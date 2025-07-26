# Make Grid filter buttons consistent with other frameworks

## Question

**Ale** asked on 16 Dec 2020

Blazor (attachment 1.jpg) jQuery (attachment 2.jpg) i would appreciate for workaround

## Answer

**Aleksandr** answered on 16 Dec 2020

workaround .k-grid-filter-popup .k-columnmenu-actions { flex-direction: row-reverse; } .k-grid-filter-popup .k-columnmenu-actions .k-button + .k-button { margin-left: 0; margin-right: 0.5rem; }

### Response

**Marin Bratanov** answered on 17 Dec 2020

Hi Aleksandr, Our current design (that we also share with our Angular and React suites) is to have the Filter button on the right. If you do want to change that, using a few lines of CSS like you found is a valid option, so I am marking this as an answer to the thread for anyone else looking for that. Regards, Marin Bratanov
