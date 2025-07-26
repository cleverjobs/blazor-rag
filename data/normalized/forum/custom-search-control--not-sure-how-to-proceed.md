# Custom Search Control- not sure how to proceed

## Question

**Bil** asked on 28 Nov 2022

I have a custom component (SearchRow) that is bound to a custom SearchParameter class. SearchParameter has IEnumerables for Fields ("Width", etc) and Operations ("Less than") as well as user-entered values. The idea being you'd select a field, an operation and enter a comparison value and that will all get passed to a service for a custom search against the database. I want to create a search bar that will be a user-addable (user clicks "Add Parameter" and a new row shows up) list of SearchRows bound to a collection of SearchParameters. Honestly I want it to look a lot like the Filter control but it seems like the Filter control is meant to act against a set of already-loaded data in a grid and I can't do that here as the searchable dataset is huge and I have to use the SearchParameter data to convert that into custom sql. Is the best way to do this to have a Grid in edit mode with a single column consisting of my SearchRow component and add to them and bind to them using OnRead?

## Answer

**Dimo** answered on 01 Dec 2022

Hi Bill, Actually, this statement is not true:>> the Filter control is meant to act against a set of already-loaded data The Filter component generates filter expressions (we call them FilterDescriptors ). You can serialize these descriptors and send them to the server to fetch only the data you need. Regards, Dimo
