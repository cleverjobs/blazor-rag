# Grid Grouping initially renders rows without grouping

## Question

**Mat** asked on 16 Jun 2025

Hello, I’m using a GroupDescriptor and have disabled LoadGroupsOnDemand for data sets under 100 records. I’ve noticed a bug where, on first render, all rows appear ungrouped for a brief moment, then “jump” into their correct groups a split-second later. When I add a debounce to the OnRead event, the issue disappears, which suggests a correlation between a heavily loaded OnRead handler and the delayed grouping. What could be causing this behavior, and has anyone encountered something similar?

### Response

**Dimo** commented on 16 Jun 2025

Hi Mateusz, I don't observe the described behavior on this test page: [https://blazorrepl.telerik.com/wzkKFgvP05cGtzZg06](https://blazorrepl.telerik.com/wzkKFgvP05cGtzZg06) Can you show what is different in your Grid setup
