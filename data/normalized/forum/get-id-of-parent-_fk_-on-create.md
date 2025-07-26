# Get ID of parent (FK) on Create

## Question

**Mic** asked on 24 Mar 2020

Hey everyone! I'm currently focusing a lot on creating components and pages with the help of Telerik Blazor UI. One problem/question that poped-up recently is the following : Let's say I have a Multi-Hierarchy grid reprensenting Orders with a list of Products for each. If i'm adding a product using a grid command column, how do i manage to get the ID of the Order under which the product was added? Thanks in advance and stay safe!

## Answer

**Svetoslav Dimitrov** answered on 24 Mar 2020

Hello Michael, In our Knowledge Base portal we have an article on performing CRUD operations in Hierarchy Grid (link: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-edit-in-hierarchy](https://docs.telerik.com/blazor-ui/knowledge-base/grid-edit-in-hierarchy) ). In this article you can see a working example of Creating, Reading, Updating and Deleting data in nested Grids and also accessing the parent model (in your case an Order) from the nested Grid (Products) by using the context and passing it to a Handler. Regards, Svetoslav Dimitrov
