# Setting the RichText editors value after OnInitializedAsync adds additional elements.

## Question

**n/an/a** asked on 30 Oct 2024

Hi, I was looking the the code at the following URL to set the value of the editor. [https://docs.telerik.com/blazor-ui/components/editor/overview](https://docs.telerik.com/blazor-ui/components/editor/overview) If I set the value to be ; <h1> Report </h1> <h2> Summary Results </h2> <h2> Results Table </h2> <table> <tbody> <tr> <th> Date Completed </th> <th> Score </th> </tr> <tr> <td> 26/03/2024 1:53:00 am </td> <td> 28.0000 </td> </tr> <tr> <td> 26/01/2024 1:46:44 am </td> <td> 48.0000 </td> </tr> <tr> <td> 26/02/2024 1:53:00 am </td> <td> 44.0000 </td> </tr> </tbody> </table> Then the results look correct as seen below; However if I set the same value via a button after OnInitializedAsync then it adds a bunch of elements and changes the report to the below Any ideas? Thanks
