import { test, expect } from '@jest/globals';
import { forceCapsInput } from '../../../../../../src/aims_ui/static/js/a_single_matches/postcode/enforce_caps_input.mjs';

// Test for the forceCapsInput function
test('Check Postcode input is converted to uppercase', () => {
  // Create a dummy input element
  const input = document.createElement('input');
  input.id = 'postcode';
  document.body.appendChild(input); // Append to document body

  // Attach the event listener
  forceCapsInput();

  // Simulate input event with lowercase value
  input.value = 'abc';
  input.dispatchEvent(new Event('input'));

  // Check if the value is converted to uppercase
  expect(input.value).toBe('ABC');
});
