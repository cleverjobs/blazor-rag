# Blazor - Gnatt - Can I access the Gnatt Timeline Columns on the code behind?

## Question

**Abb** asked on 29 Jan 2025

Is there a way that I can loop through the Columns of the Gnatt chart to access the attributes on the code behind? For example, I want to see if Column D has been moved or hidden. The closest thing I can see if GanttColumns but I cannot look through it because it is a RenderFragment? var columns=Ref.GanttColumns; I saw on the object ColumnsCollection which is ideal but it's not a public attribute for me to query it. Any ideas?

## Answer

**Tsvetomir** answered on 31 Jan 2025

Hello Abby, To access and manipulate the Gantt columns programmatically, you can utilize the Gantt State. To loop through the Gant Columns, use the ColumnStates collection through the Gantt state. This will allow you to get current columns visibility, order, field, etc. I recommend referring to the linked documentation to gather more information about it and see an example. I hope the provided information serves you well. Regards, Tsvetomir Progress Telerik
