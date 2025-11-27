import { test, expect } from '@jest/globals';
import {
  getChosenTitleId,
  getUserFriendlyPreference,
  getAddressTitle,
} from '../../../../../../src/aims_ui/static/js/e_all_pages/apply_custom_settings.mjs';

// Test Match Type Verbose Description
test('Match Type Verbose Description For Single Match', () => {
  const matchType = 'S';
  const matchTypeDescription = getMatchTypeDescription(matchType);

  expect(matchTypeDescription).toBe(
    'S - Single match with Confidence Score above threshold'
  );
});

test('Match Type Verbose Description For Multiple Matches', () => {
  const matchType = 'M';
  const matchTypeDescription = getMatchTypeDescription(matchType);

  expect(matchTypeDescription).toBe(
    'M - Multiple Matches with Confidence Score above threshold'
  );
});

test('Match Type Verbose Description For No Matches', () => {
  const matchType = 'N';
  const matchTypeDescription = getMatchTypeDescription(matchType);

  expect(matchTypeDescription).toBe(
    'N - No matches with Confidence Score above threshold'
  );
});

// Test Recommendation Code Verbose Description
test('Recommendation Code Verbose Description For Accept', () => {
  const recommendationCode = 'A';
  const recommendationCodeDescription =
    getRecommendationCodeDescription(recommendationCode);

  expect(recommendationCodeDescription).toBe('A - Accept the top result');
});

test('Recommendation Code Verbose Description For Investigate', () => {
  const recommendationCode = 'I';
  const recommendationCodeDescription =
    getRecommendationCodeDescription(recommendationCode);

  expect(recommendationCodeDescription).toBe('I - Investigate results');
});

// Test Get Chosen Title Id
test('Get Chosen Title Prefference Paf', () => {
  const preference = 'paf';
  const titleId = getChosenTitleId(preference);

  expect(titleId).toBe('formattedAddressPaf');
});

test('Get Chosen Title Prefference Nag', () => {
  const preference = 'nag';
  const titleId = getChosenTitleId(preference);

  expect(titleId).toBe('formattedAddressNag');
});

test('Get Chosen Title Prefference Undeffined By User', () => {
  const preference = '';
  const titleId = getChosenTitleId(preference);

  expect(titleId).toBe('formattedAddress');
});

// Test getUserFriendlyPreference
test('Get User Friendly Preference Def (default)', () => {
  const preference = 'def';
  const userFriendlyPreference = getUserFriendlyPreference(preference);

  expect(userFriendlyPreference).toBe('');
});

test('Get User Friendly Preference Paf', () => {
  const preference = 'paf';
  const userFriendlyPreference = getUserFriendlyPreference(preference);

  expect(userFriendlyPreference).toBe(' (PAF Formatting)');
});

test('Get User Friendly Preference Nag', () => {
  const preference = 'nag';
  const userFriendlyPreference = getUserFriendlyPreference(preference);

  expect(userFriendlyPreference).toBe(' (NAG Formatting)');
});

// Test address title aquisition
const testAddressTitles = [ 
  {id: 'formattedAddressPaf', title: 'PAF address example'},
  {id: 'formattedAddressNag', title: 'NAG address example'},
  {id: 'formattedAddress', title: 'Default Address'},
]

test('Get Address Title Paf', () => {
  const title = getAddressTitle('paf', testAddressTitles);

  expect(title).toBe(testAddressTitles[0]);
});

test('Get Address Title Nag', () => {
  const title = getAddressTitle('nag', testAddressTitles);

  expect(title).toBe(testAddressTitles[1]);
});

test('Get Address Title Default', () => {
  const title = getAddressTitle('', testAddressTitles);

  expect(title).toBe(testAddressTitles[2]);
});
