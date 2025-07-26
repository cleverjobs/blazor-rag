# FooterTemplate throws error

## Question

**Nic** asked on 17 Sep 2020

When attempting to implement a Footer Template on a Grid Column, I am getting the following runtime errors: "Unhandled exception rendering component: Value cannot be null" and "Unhandled exception rendering component: Object reference not set to an instance of an object". I have tried something as simple as <FooterTemplate> Test </FooterTemplate> And I still get that error, otherwise I get no errors on rendering the page without the FooterTemplate tags within the Grid Column.

## Answer

**Marin Bratanov** answered on 17 Sep 2020

Hello Nick, My best guess is that the project references an older version that does not recognize the footer - it is available in 2.17.0. If you have updated the package reference, try cleaning the project, even deleting the bin and obj folders - sometimes old versions get cached there. If this does not help, I recommend opening a ticket where you can send is a simple runnable project that shows the problem so we can have a look at it. Regards, Marin Bratanov

### Response

**Cesar Augusto** answered on 02 Oct 2020

i get this error. Error: System.ArgumentNullException: Value cannot be null. (Parameter 'source')

### Response

**Marin Bratanov** answered on 02 Oct 2020

Hi Cesar, You can Follow a fix for this and see a workaround (initializing the Data collection of the grid so it is not null) here: [https://feedback.telerik.com/blazor/1486142-footertemplate-throws-when-grid-data-is-null](https://feedback.telerik.com/blazor/1486142-footertemplate-throws-when-grid-data-is-null) Regards, Marin Bratanov
