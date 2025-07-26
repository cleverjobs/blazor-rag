# Remove example from filter row

## Question

**Pau** asked on 08 Sep 2022

Hi I have a date field in a grid, and the filter row, how can i remove the automatically created 'd-M-yyyy' placeholder from the filter cell?

### Response

**Paul** commented on 08 Sep 2022

I see [https://www.telerik.com/forums/placeholder-question](https://www.telerik.com/forums/placeholder-question) It should be resolved but I cant find the documentation for it Eric

## Answer

**Tsvetomir** answered on 12 Sep 2022

Hi Eric, The linked feedback item targets the date inputs in general. For the date picker, the Placeholder has been documented as part of its built-in options in its Overview docs article. However, since the picker is used internally by the row filter, I can recommend setting a custom component in the filter cell and specifying the Placeholder explicitly. The custom filter row demo can be used as a base for the implementation. Let me know if additional information is needed. Kind regards, Tsvetomir
