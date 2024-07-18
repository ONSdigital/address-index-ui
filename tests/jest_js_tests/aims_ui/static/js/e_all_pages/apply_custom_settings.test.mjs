import { test, expect } from '@jest/globals';
import {
  getMatchTypeDescription,
} from '../../../../../../src/aims_ui/static/js/e_all_pages/apply_custom_settings.mjs';


test('Match Type Verbose Description For Single Match', () => {
  const matchType = 'S';
  const matchTypeDescription = getMatchTypeDescription(matchType);

  expect(matchTypeDescription).toBe('S - Single match with Confidence Score above threshold');
});

test('Match Type Verbose Description For Multiple Matches', () => {
  const matchType = 'M';
  const matchTypeDescription = getMatchTypeDescription(matchType);

  expect(matchTypeDescription).toBe('M - Multiple Matches with Confidence Score above threshold');
});

test('Match Type Verbose Description For No Matches', () => {
  const matchType = 'N';
  const matchTypeDescription = getMatchTypeDescription(matchType);

  expect(matchTypeDescription).toBe('N - No matches with Confidence Score above threshold');
});
