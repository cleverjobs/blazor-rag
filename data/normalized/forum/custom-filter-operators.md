# Custom Filter Operators

## Question

**Phi** asked on 16 May 2022

It would be greatly beneficial to our projects if there were enhancements to the Filter component to allow for supplying custom Filter Operators. For example, our legacy software provided native "Between" operator support along with custom "Date Range" operators, such as "today", "Yesterday", "This Week", etc. While I wouldn't expect Telerik to support these out of the box, it would be great to be able to add our own operators/Filter types.

## Answer

**Tsvetomir** answered on 18 May 2022

Hi, Phil, Thank you for taking the time to share your feedback. Currently, the Filter component is intended to have only strongly-typed filter operator values, more specifically, the operator should be of type FilterOperator Enum. It comes with a set of predefined values for all built-in operators. If we were to expose an option to add a custom operator, it would break the strongly-typed orientation of the component. Currently, we have a pending Feature Request in our

### Response

**Víctor** commented on 09 Mar 2023

I would also like to extend the default filters. Why not using a class hierarchy instead of an enum? This way we could add out own subclases. I need my users to be able to have dropdowns for related entities.

### Response

**Tsvetomir** commented on 13 Mar 2023

I recommend sharing your opinion and feedback directly in the feature request's item so that whenever a developer starts working and researching, they'll implement it in such a way that is helpful for all: [https://feedback.telerik.com/blazor/1561874-filter-field-template](https://feedback.telerik.com/blazor/1561874-filter-field-template)
