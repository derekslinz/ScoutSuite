import json
import os
import tempfile
import unittest

from ScoutSuite.core.console import set_logger_configuration, print_error
from ScoutSuite.core.processingengine import ProcessingEngine
from ScoutSuite.core.ruleset import Ruleset


class DummyObject(object):
    pass


class TestAliyunProvider(unittest.TestCase):

    def setUp(self):
        set_logger_configuration(is_debug=True)
        self.rule_counters = {'found': 0, 'tested': 0, 'verified': 0}
        self.test_dir = os.path.dirname(os.path.realpath(__file__))

    def test_all_finding_rules(self):
        ruleset_file_name = os.path.join(self.test_dir, '../ScoutSuite/providers/aliyun/rules/rulesets/cis.json')
        with open(ruleset_file_name, 'rt') as f:
            ruleset = json.load(f)

        for rule_file_name in ruleset['rules']:
            self.rule_counters['found'] += 1
            rule = ruleset['rules'][rule_file_name][0]
            rule['enabled'] = True
            print(rule_file_name)
            self._test_rule(rule_file_name, rule)

        print('Existing  rules: %d' % self.rule_counters['found'])
        print('Processed rules: %d' % self.rule_counters['tested'])
        print('Verified  rules: %d' % self.rule_counters['verified'])

    def _test_rule(self, rule_file_name, rule):
        test_config_file_name = os.path.join(self.test_dir, 'data/rule-configs/aliyun/%s' % rule_file_name)
        if not os.path.isfile(test_config_file_name):
            return
        self.rule_counters['tested'] += 1

        ruleset = self._generate_ruleset(rule_file_name, rule)
        pe = ProcessingEngine(ruleset)

        dummy_provider = DummyObject()
        dummy_provider.services = {}
        with open(test_config_file_name, 'rt') as f:
            test_config_dict = json.load(f)
            for key in test_config_dict:
                setattr(dummy_provider, key, test_config_dict[key])
        service = rule_file_name.split('-')[0]
        dummy_provider.services = {service: {}}
        dummy_provider.service_list = [service]
        pe.run(dummy_provider)
        findings = dummy_provider.services[service]['findings']

        test_result_file_name = os.path.join(self.test_dir, 'data/rule-results/aliyun/%s' % rule_file_name)
        if not os.path.isfile(test_result_file_name):
            print_error('Expected findings:: ')
            print_error(json.dumps(findings, indent=4))
            return

        self.rule_counters['verified'] += 1
        with open(test_result_file_name, 'rt') as f:
            items = json.load(f)

        try:
            self.assertEqual(findings, items)
        except Exception:
            print_error('Expected items:\\n %s' % json.dumps(items, indent=4))
            print_error('Reported items:\\n %s' % json.dumps(findings, indent=4))
            raise

    def _generate_ruleset(self, rule_file_name, rule):
        test_ruleset = {'rules': {}, 'about': 'regression test'}
        test_ruleset['rules'][rule_file_name] = [rule]

        with tempfile.NamedTemporaryFile('wt', delete=False) as f:
            f.write(json.dumps(test_ruleset, indent=4))

        return Ruleset(cloud_provider='aliyun', filename=f.name)
