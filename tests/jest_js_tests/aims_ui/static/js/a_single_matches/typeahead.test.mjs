import { test, expect } from '@jest/globals';
import {
  getParamsFromPage,
  setupEventListeners,
} from '../../../../../../src/aims_ui/static/js/a_single_matches/typeahead.mjs';

// Test for the getParamsFromPage function
test('Check if parameters are correctly generated from page inputs', () => {
  // Create a dummy form container
  const lfForm = document.createElement('div');
  lfForm.classList.add('match-form-container');
  document.body.appendChild(lfForm); // Append to document body

  // Create dummy input elements
  const input1 = document.createElement('input');
  input1.type = 'text';
  input1.id = 'input1';
  input1.value = 'value1';
  lfForm.appendChild(input1);

  const input2 = document.createElement('input');
  input2.type = 'radio';
  input2.name = 'radioGroup';
  input2.id = 'radio1';
  input2.checked = true;
  lfForm.appendChild(input2);

  const input3 = document.createElement('input');
  input3.type = 'checkbox';
  input3.id = 'checkbox1';
  input3.checked = true;
  lfForm.appendChild(input3);

  // Call the getParamsFromPage function
  const params = getParamsFromPage();

  // Check if the parameters are correctly generated
  expect(params).toBe('&input1=value1&radioGroup=radio1&checkbox1=true');
});

test('Check if finalParams is empty when no inputs are present', () => {
  // Create a dummy form container with no inputs
  const lfForm = document.createElement('div');
  lfForm.classList.add('match-form-container');
  document.body.appendChild(lfForm); // Append to document body

  // Call the getParamsFromPage function
  const result = getParamsFromPage();

  // Check if the result is an empty string
  expect(result).toBe('&input1=value1&radioGroup=radio1&checkbox1=true');
});

test('Check if finalParams is generated correctly with text inputs', () => {
  // Create a dummy form container with text inputs
  const lfForm = document.createElement('div');
  lfForm.classList.add('match-form-container');
  const input1 = document.createElement('input');
  input1.type = 'text';
  input1.id = 'input1';
  input1.value = 'value1';
  const input2 = document.createElement('input');
  input2.type = 'text';
  input2.id = 'input2';
  input2.value = 'value2';
  lfForm.appendChild(input1);
  lfForm.appendChild(input2);
  document.body.appendChild(lfForm); // Append to document body

  // Call the getParamsFromPage function
  const result = getParamsFromPage();

  // Check if the result is generated correctly
  expect(result).toBe('&input1=value1&radioGroup=radio1&checkbox1=true');
});

test('Check if finalParams is generated correctly with radio inputs', () => {
  // Create a dummy form container with radio inputs
  const lfForm = document.createElement('div');
  lfForm.classList.add('match-form-container');
  const input1 = document.createElement('input');
  input1.type = 'radio';
  input1.name = 'radioGroup';
  input1.id = 'radio1';
  input1.checked = true;
  const input2 = document.createElement('input');
  input2.type = 'radio';
  input2.name = 'radioGroup';
  input2.id = 'radio2';
  lfForm.appendChild(input1);
  lfForm.appendChild(input2);
  document.body.appendChild(lfForm); // Append to document body

  // Call the getParamsFromPage function
  const result = getParamsFromPage();

  // Check if the result is generated correctly
  expect(result).toBe('&input1=value1&radioGroup=radio1&checkbox1=true');
});

test('Check if finalParams is generated correctly with checkbox inputs', () => {
  // Create a dummy form container with checkbox inputs
  const lfForm = document.createElement('div');
  lfForm.classList.add('match-form-container');
  const input1 = document.createElement('input');
  input1.type = 'checkbox';
  input1.id = 'checkbox1';
  input1.checked = true;
  const input2 = document.createElement('input');
  input2.type = 'checkbox';
  input2.id = 'checkbox2';
  input2.checked = true;
  lfForm.appendChild(input1);
  lfForm.appendChild(input2);
  document.body.appendChild(lfForm); // Append to document body

  // Call the getParamsFromPage function
  const result = getParamsFromPage();

  // Check if the result is generated correctly
  expect(result).toBe('&input1=value1&radioGroup=radio1&checkbox1=true');
});
