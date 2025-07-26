# Blazor Grid Not Displaying Data from List

## Question

**Bil** asked on 03 Apr 2024

I have a Blazor Grid in .NET 8 that binds to a List<> called GridData the I fill in OniIntializedAsync(). The data returns fine and the grid shows the correct number of rows, but none of the columns show their data. I tried AutoGenerateColmns-"true" and setting the <GrdiColumns>. If I loop the List with foreach, the data displays as expected.

### Response

**Bill** commented on 03 Apr 2024

Figured this out. Bound columns require a public getter for read and setter for write. I am using records which have implied get/set. Adding explicit { get; set; } solves the problem.

### Response

**Hristian Stefanov** commented on 04 Apr 2024

Hi Bill, I'm happy to see you quickly resolved the matter on your own. Thank you for publicly sharing it so other developers in the same situation can benefit from it. Kind Regards, Hristian

### Response

**Rob** commented on 27 Nov 2024

I had the exact same issue, thank you for the solution. I just assumed that because my other bound Telerik controls (TextBox) didn't require the Set; Get; for properties in my model then I wouldn't need to do it for Telerik grid. Might qualify for Telerik documentation tips/tricks update? Rob.

### Response

**Hristian Stefanov** commented on 28 Nov 2024

Hi Rob, I'm glad to hear that this public discussion helped you as well. Additionally, you're absolutely right that this behavior can sometimes feel inconsistent when working with different types of components. However, the need for "get;" "set;" accessors in bound properties is actually a general Blazor requirement for data binding, rather than something specific to Telerik components. The examples provided in our Grid documentation already demonstrate this practice, which serves as a helpful hint for such scenarios. Still, we’re always striving to improve our documentation, and I’ll take note of your suggestion and see whether we can put something like that in the future. Kind Regards, Hristian
