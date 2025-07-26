# Grid Pageable option generates "Unhandled exception rendering component: Value cannot be null. (Parameter 'format')"

## Question

**Sté** asked on 15 Jul 2021

Hi, I'm using the Trial 2.25.0 with the Telerik project template. When I try to access the Grid demo page I get the error "Unhandled exception rendering component: Value cannot be null. (Parameter 'format')". I narrowed down the error to the Pageable option. If I don't use it then the page is fine but there's no pagination. * Microsoft Visual Studio Enterprise 2019 Version 16.10.3 * Chrome Version 91.0.4472.124 I have no clue on what could be wrong because the same option is used (roughly in the same way) in GitHub-paste-from-excel. I attached the following screenshots: ProjectTemplate: Shows the telerik template I used for generating the project. It's available after installing the Trial. Grid: The link I used in the main page. PageableDisabled: Disabling the Pageable option. GridPage: The grid but without pagination. Pageable: Pageable option is enabled. GridPageError: The exception in the browser console. Thanks

### Response

**Stéphane** commented on 15 Jul 2021

Hi, Comparing with [https://www.telerik.com/forums/grid-pageable-system-argumentnullexception-value-cannot-be-null,](https://www.telerik.com/forums/grid-pageable-system-argumentnullexception-value-cannot-be-null,) I noticed that I added resources files for a small test with the Form page. Creating another projet with the Telerik template without adding resources files is fine, the grid page has the pagination. This means that all I need is the list of resources that I must add to the existing resource files. Thanks

### Response

**Stéphane** commented on 15 Jul 2021

Hi, I looked at the sceenshot available at [https://www.telerik.com/forums/grid-pageable-system-argumentnullexception-value-cannot-be-null](https://www.telerik.com/forums/grid-pageable-system-argumentnullexception-value-cannot-be-null) and I added the "Pager_*" resources. It's all good now! That was a weird one that I consider almost like a bug. Thanks

## Answer

**Stéphane** answered on 16 Jul 2021

To close. Thanks
