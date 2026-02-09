import { getPagePreviouslySearchedValues } from "../../e_all_pages/save_and_restore_input_helpers/set_and_get_data.mjs";

export function getPostBodyTextBoxStyleFromLocalStorage() {
  const previouslySearchedValues = getPagePreviouslySearchedValues('custom_response');
  const postBodyTextBoxStyle = previouslySearchedValues['post-body-style'];

  if (!postBodyTextBoxStyle) {
    console.debug('No previously stored style for post body textbox found in local storage.');
  }

  return postBodyTextBoxStyle || '';
}