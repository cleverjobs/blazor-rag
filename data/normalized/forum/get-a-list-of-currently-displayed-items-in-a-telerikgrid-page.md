# Get a List of currently displayed items in a TelerikGrid Page

## Question

**Rém** asked on 23 Feb 2022

Hello, I'm currently using the TelerikGrid component from Telerik UI for blazor, and I would like to know if there's a possibility of retrieving the currently displayed data on a page. For example if I got 24 data and set the PageSize to 18, is there a way to get a list of the 18 data displayed on the first page and when going to second page, get a list of the 6 data on this page ? Thanks in advance Rémy Macherel

## Answer

**Marin Bratanov** answered on 23 Feb 2022

Hello Rémy, This article shows how you can do this: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-get-filtered-data](https://docs.telerik.com/blazor-ui/knowledge-base/grid-get-filtered-data) Regards, Marin Bratanov

### Response

**Rémy** commented on 28 Feb 2022

Hi thanks for your answer, I still got a problem, when using your example, the args (GridReadEventArgs) does not contain a definition for Data and Total. I looked on the using but I seem to have them all the same as in your example. I'm using Telerik UI for blazor 2.25 Kind regards Rémy Macherel

### Response

**Rémy** commented on 28 Feb 2022

I also tried only importing the example code in an other project and the same problem persists. The args has no definition for Data and Total properties. Am I missing something ? Rémy

### Response

**Marin Bratanov** commented on 28 Feb 2022

The current code is for versions 3.0.0 and later, your version still does not have that. You should upgrade to the latest (also, take a look at this ).
