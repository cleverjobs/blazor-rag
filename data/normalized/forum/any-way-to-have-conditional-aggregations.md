# Any way to have conditional aggregations?

## Question

**Ale** asked on 04 Nov 2020

for example Count by FieldValue=="X" ???

## Answer

**Marin Bratanov** answered on 04 Nov 2020

Hello Aleksandr, I am not sure I understand the question, but you have have you own (custom,conditional) aggregates by calculating them yourself and showing those values in the footer. The example in the Notes section of the Column Footer article shows one example of this: [https://docs.telerik.com/blazor-ui/components/grid/templates/column-footer#notes](https://docs.telerik.com/blazor-ui/components/grid/templates/column-footer#notes) Regards, Marin Bratanov

### Response

**Jon** answered on 26 May 2022

Hack example (I am wanting to do the same thing, count items in a column ONLY if a certain criteria is true): <FooterTemplate> @ClassRoster.SelectMany(x=> x.ScheduleDays.Where(t=> t.DayOfWeekInt==(int)DayOfWeekValueEnum.Monday)).ToList().Count </FooterTemplate>
