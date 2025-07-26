# Grid filters

## Question

**Evg** asked on 11 May 2021

I've noticed a strange bechavior of the grid filtering when pageable is true. When grid initialized, we show records by 10 per page, paging works fine, filtering as well. But, if grid is filtered by some value and we press the button to clear a filtering value, pageable doesn't work, grid loads all data at once. There are a lot of rows and grid freezes a few seconds. How can we fix it, so after clear filters value, grid show data by page?

### Response

**Dimo** commented on 12 May 2021

Hi Evgeny, The described behavior is strange indeed. I tested a couple of our online demos and they seem to work fine, so I will need more information to provide a suggestion. Please check the following examples and let me know the exact steps if you can reproduce the issue there: [https://demos.telerik.com/blazor-ui/grid/filter-row](https://demos.telerik.com/blazor-ui/grid/filter-row) [https://demos.telerik.com/blazor-ui/grid/manual-operations](https://demos.telerik.com/blazor-ui/grid/manual-operations) If the above pages work as expected, please share the following information: - UI for Blazor version - Grid declaration and relevant data binding code Thanks!
