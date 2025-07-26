# How to set grid to a class with an unknown set of columns?

## Question

**Dea** asked on 07 Nov 2023

Not sure if this is possible. Hopefully someone can point me in right direction. I have a report with a set of columns in beginning and end. And within the center of the report is a set of columns that I wont know how many. Example: Col1, col2 , col3, col*, cola, colb, colc, etc.... Col*=1 to many. Each row is an order and the Col* represents items on the order. I take it the telerik grid would have to be set to autogenerate the columns for the grid. I am just not sure how I build the Class for the report result in this case. public class RtpOrderItems { public string? Col1 { get; set; } public string? Col1 { get; set; } public string? Col1 { get; set; } public string? Col* { get; set; } // ? How would u go about this piece. Closest I came is the Dictionary field but I could get it to work. public string? ColA { get; set; } public string? ColB { get; set; } public string? ColC { get; set; } } Thanks in advance

### Response

**Dimo** commented on 09 Nov 2023

Using Dictionary is very similar to ExpandoObject Grid binding and you can see the linked KB article for inspiration how to configure the Grid. You may also need to foreach Grid columns at runtime, which is also possible.

### Response

**Deasun** commented on 14 Nov 2023

Thanks. Gives me something to look at. :)
