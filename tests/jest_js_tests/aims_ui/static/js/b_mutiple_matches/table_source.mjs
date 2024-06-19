export function getTableElement(rows) {
  const table = document.createElement('table');
  table.id = 'adjustLinksTable';
  table.className = 'ons-table ons-table--responsive';

  const caption = document.createElement('caption');
  caption.className = 'ons-table__caption';
  caption.textContent = 'Jobs';
  table.appendChild(caption);

  const thead = document.createElement('thead');
  thead.className = 'ons-table__head';
  const headerRow = document.createElement('tr');
  headerRow.className = 'ons-table__row';

  const headers = [
    'JOBID',
    'NAME',
    'STATUS',
    'USER ID',
    'HEADER ROW',
    'RECS PROCESSED',
    'DOWNLOAD LINK',
  ];
  headers.forEach((headerText) => {
    const th = document.createElement('th');
    th.scope = 'col';
    th.className = 'ons-table__header';
    const span = document.createElement('span');
    span.className = 'ons-table__header-text';
    span.textContent = headerText;
    th.appendChild(span);
    headerRow.appendChild(th);
  });

  thead.appendChild(headerRow);
  table.appendChild(thead);

  const tbody = document.createElement('tbody');
  tbody.className = 'ons-table__body';

  rows.forEach((row) => {
    const tr = document.createElement('tr');
    tr.className = 'ons-table__row';
    for (const key in row) {
      const td = document.createElement('td');
      td.className = 'ons-table__cell';
      const content = row[key];
      if ('<a>'.includes(content)) {
        // Create a link element
        const link = document.createElement('a');
        link.href = 'TestLink';
        link.textContent = 'TestLink';
        td.appendChild(link);
      } else {
        td.textContent = row[key];
      }
      tr.appendChild(td);
    }
    tbody.appendChild(tr);
  });

  table.appendChild(tbody);
  return table;
}
