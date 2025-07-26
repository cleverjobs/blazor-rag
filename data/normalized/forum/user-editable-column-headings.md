# User Editable Column Headings

## Question

**Kel** asked on 22 Nov 2020

I would like to allow the user to add columns to the grid. When they add a column, they will need to add/edit the column header text. I have tried to add a textbox to a HeaderTemplate, but was not able to get it to respond to click event. Basically, when the user clicks on the title it should go into edit mode. Then, when they click away or hit enter the header will exit edit mode.

## Answer

**Marin Bratanov** answered on 22 Nov 2020

Hi Kelly, The built-in column chooser in the column menu can let you declare the columns in the markup, and mark some of them as Visible=false so they are not rendered, and the user can turn them on on their own. As for clicks in the header template - you should probably prevent them from going up the DOM because they have a default action sorting the grid - which will re-render the grid and effectively can prevent your own logic from running. Regards, Marin Bratanov

### Response

**Kelly** answered on 22 Nov 2020

Hi Marin, Thank you for the quick response. Maybe I was not clear in my explanation. The workflow I am trying to create is a user-defined columns similar to Monday.com boards. The user would be able to select a column "template" and define it as whatever they choose. Therefore they need to be able to define the column heading. I would then store the heading text in the database. The column chooser would only be of value after they have defined the column. -Kelly

### Response

**Marin Bratanov** answered on 22 Nov 2020

Hi Kelly, Perhaps you could use a new grid with columns for the options you want the user to define, and you can bind it to the collection of column descriptors you'll have, something similar to my sample from this thread: [https://feedback.telerik.com/blazor/1450105-column-chooser](https://feedback.telerik.com/blazor/1450105-column-chooser) Regards, Marin Bratanov

### Response

**Kelly** answered on 27 Dec 2020

Thank you for the Reply Marin. I am trying to recreate the Monday.com boards and mimic the ability for users to create columns (which includes defining the title of the column). This is a feature that my users have been asking for and Monday.com has definitely moved the innovation needle in this area. I would encourage you to look at what they have done. I have been asked many times what Progress can do to bring value to your customers. I have been very vocal on Progress not just providing "me too" controls, but rather innovate on new ways to express UI. I am using abp.io on this project and they provide Blazorise controls. I find it hard to justify a $1100+ value in the "me too" controls. Don't get me wrong I am a committed Progress customer and would like to continue to support your efforts, but in my opinion, without innovating you will quickly become obsolete. I know you all are doing a lot to accommodate your customer requests and my intent is to provide a customer perspective on what features are becoming expectations from my customers.

### Response

**Marin Bratanov** answered on 28 Dec 2020

Hi Kelly, The grid takes the header text either from the Title parameter of the column definition, or from the Display Name from the model (which you can, by the way, localize, see here for an example, perhaps you could use a similar approach to read titles). So, the grid takes what the developer provides and that is usually tied to a data model that describes the grid data, not so much its UI. Thus, the general approach is to make sure your app defines the desired models and their data. The grid itself is supposed to edit only the model data it shows, and the rest of its UI is up to the developer where templates are provided (which is just about all places, probably the pager is the only one that does not have templates yet). Editing titles is an operation that is not defined in the data model of the grid - storing that information is something that the application needs to do, and so it is a completely separate task from handling the main data set. As such, this operation is undefined and heuristic for the grid, and should be implemented entirely through templates, our components can't have heuristic tasks. While I understand your goal and I thank you for your input, we still need to be careful to add features that can be reusable and clearly defined so they can serve a multitude of users. Thus, my advice is to create a component that lets you edit the titles and knows how to save/obtain those titles, then simply put it in the header template of each column you want editable. Just cancel the click events for it as described here. You may also find interesting this article on reusing templates. Another approach I can suggest is that you add the title editing capabilities in the custom column chooser you need to make to let your users define your models anyway (you can find a basic example of that here in my post from 21 Jan 2020, just add more columns and editing capabilities to that grid). This will allow you to implement the desired logic for generating models (or expando object collections, depending on how your app works with its data, and also to define the storage for the custom titles per user). Regards, Marin Bratanov
