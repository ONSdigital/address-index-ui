function widenCheckboxes() {
  let children = document.querySelectorAll('.ons-radios__items > *');

  let nodesArray = Array.from(children);
  let spans = nodesArray.filter((node) => node.nodeName === 'SPAN');

  for (let i = 0; i < children.length; i++) {
    let style = children[i].getAttribute('style');
    if (style) {
      style = style.replace('width: auto', 'width: 100%');
      children[i].setAttribute('style', style);
    }
  }
}

export function allPagesLastInit() {
  console.log('all_pages_last loaded');
  widenCheckboxes();
}
