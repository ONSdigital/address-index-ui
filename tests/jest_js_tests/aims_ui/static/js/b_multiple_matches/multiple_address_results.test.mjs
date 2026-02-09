import { test, expect } from '@jest/globals';
import {
  findIfPafOrNagWasUsed,
} from '../../../../../../src/aims_ui/static/js/b_multiple_matches/multiple_address_results/multiple_address_results.mjs';

test('Paf or Nag Selector tests', () => {
  const pafAddress = {
    formattedAddress: 'NA address example',
    pafAddress: 'PAF address example',
    nagAddress: 'NAG address example',
  };

  const detectedPafOrNag = findIfPafOrNagWasUsed(pafAddress);

  // Expect the result to be PAF
  expect(detectedPafOrNag).toBe('N/A');
});
