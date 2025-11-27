import { getRecommendationCodeDescription } from '../../../../../../src/aims_ui/static/js/macros/custom_additional_request_info/content_generation_recommendation_code.mjs';

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

