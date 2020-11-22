from tgalice.nlu.matchers import make_matcher_with_regex, TFIDFMatcher
from tgalice.nlu.regex_expander import load_intents_with_replacement


def test_expander():
    intents = load_intents_with_replacement(
        'tests/test_nlu/intents.yaml',
        'tests/test_nlu/expressions.yaml'
    )
    matcher = make_matcher_with_regex(TFIDFMatcher(), intents=intents)
    assert matcher.match('take number 10')
