# Add GridView columns in front of DetailTemplate drop down column

## Question

**Cha** asked on 28 Mar 2024

I have a TelerikGrid that contains many columns and a DetailTemplate within it. The Grid has functionality for multiselect with a checkbox column that appears as the first column on the grid. Is it possible to move this checkbox column in front of the detail template '+' dropdown row? <TelerikGrid data="@models" <DetailTemplate> <GridColumns> <GridColumns /> <DetailTemplate /> <GridColumns> <GridColumn> Checkbox Here <GridColumn /> <GridColumns /> <TelerikGrid />

## Answer

**Hristian Stefanov** answered on 02 Apr 2024

Hi Chase, The ability to reorder the expand ("+") column sounds like a good idea for an enhancement in the Grid. Thus, I submitted a feature request on your behalf for this functionality on our Public Feedback Portal: Ability to control the position of the expand ("+") column in a Hierarchical Grid. You are automatically subscribed as a creator to receive email notifications for status updates. In the meantime, if an alternative appears, I will share it as a comment on the above public item. Regards, Hristian Stefanov Progress Telerik
