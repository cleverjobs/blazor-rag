# GridCheckboxColumn make all check boxes Checked on Load

## Question

**con** asked on 17 Jun 2020

Hi, How do I make all/some Check Boxes selected on Grid Load? Is there "Value" or "Selected" property of that component? Something like: <GridColumns> <GridCheckboxColumn Selected="true"/> </GridColumns> Please advise

## Answer

**const** answered on 18 Jun 2020

OK, I found the answer in posts: [https://www.telerik.com/forums/checkbox-column-f1b24f092353#vwso5nJgMU6DijCGVMzx8Q](https://www.telerik.com/forums/checkbox-column-f1b24f092353#vwso5nJgMU6DijCGVMzx8Q) The summary is: "The GridCheckboxColumn is used only for row selection, not for data binding/display." Then I have another question: is there a way to select Row(s) from code during Grid rendering?

### Response

**Marin Bratanov** answered on 18 Jun 2020

Hello, The Blazor way of doing that is to use a collection that controls the selected items. Please start by reviewing the available documentation we have on that: [https://docs.telerik.com/blazor-ui/components/grid/selection/overview](https://docs.telerik.com/blazor-ui/components/grid/selection/overview) [https://docs.telerik.com/blazor-ui/components/grid/selection/multiple](https://docs.telerik.com/blazor-ui/components/grid/selection/multiple) So, you can populate the SelectedItems collection when fetching the data which happens before the grid renders. Another alternative is using the grid state to store the user choice or to populate selected items there: [https://docs.telerik.com/blazor-ui/components/grid/state.](https://docs.telerik.com/blazor-ui/components/grid/state.) As for the name of the column and how it works, you may find interesting the following requests, so you can Vote for them to raise their priority and Follow them to know when they get implemented: on displaying boolean values in a bound column with a checkbox by default: [https://feedback.telerik.com/blazor/1454768-blazor-grid-boolean-checkbox-display](https://feedback.telerik.com/blazor/1454768-blazor-grid-boolean-checkbox-display) on a breaking change that will change the name of the current checkbox column to something that denotes it is about selection of rows: [https://feedback.telerik.com/blazor/1454771-rename-confusing-gridcheckboxcolumn](https://feedback.telerik.com/blazor/1454771-rename-confusing-gridcheckboxcolumn) [https://feedback.telerik.com/blazor/1441291-ability-to-enable-disable-checkbox-in-checkbox-column-to-allow-prevent-selection-of-the-row](https://feedback.telerik.com/blazor/1441291-ability-to-enable-disable-checkbox-in-checkbox-column-to-allow-prevent-selection-of-the-row) [https://feedback.telerik.com/blazor/1454469-select-rows-only-with-checkboxes-clicking-the-rows-to-not-affect-selection](https://feedback.telerik.com/blazor/1454469-select-rows-only-with-checkboxes-clicking-the-rows-to-not-affect-selection) Regards, Marin Bratanov

### Response

**const** answered on 18 Jun 2020

Grid State is really great and powerful method of Grid management! Great implementation of Great Idea, Gents! So, as I understood, I'm still able to manipulate a Grid values. Like here: [https://demos.telerik.com/blazor-ui/](https://demos.telerik.com/blazor-ui/) (Edit Item demo): async Task EditItemFour() { var currState=GridRef.GetState(); // reset any current insertion and any old edited items. Not mandatory. currState.InsertedItem=null; // add item you want to edit to the state, then set it to the grid SampleData itemToEdit=SampleData.GetClonedInstance(MyData.Where(itm=> itm.ID==4).FirstOrDefault()); // you can alter values here as well (not mandatory) itemToEdit.Name="Changed from code"; currState.OriginalEditItem=itemToEdit; // for InCell editing, you can use the EditField property instead await GridRef.SetState(currState); } Or GridCheckboxColumn is exemption? Please advise.

### Response

**const** answered on 18 Jun 2020

... just to make it clear: I'm referencing Components/Grid/Grid State demo in post above ...

### Response

**Marin Bratanov** answered on 18 Jun 2020

Hello, The GridCheckboxColumn is NOT a data column, it does not show data. It is all about selection of rows: [https://feedback.telerik.com/blazor/1454771-rename-confusing-gridcheckboxcolumn.](https://feedback.telerik.com/blazor/1454771-rename-confusing-gridcheckboxcolumn.) So, to make those checkboxes selected, you must select rows. You can see how to do that here: [https://docs.telerik.com/blazor-ui/components/grid/selection/multiple#two-way-binding-of-selecteditems.](https://docs.telerik.com/blazor-ui/components/grid/selection/multiple#two-way-binding-of-selecteditems.) If you want to pre-set editor values - then you must use a regular <GridColumn> and the values there will depend on the model values, so you don't have to use the state to alter them in the general case, doing it like in the example you copied might make sense in particular scenarios like upon editing/inserting based on some custom logic. Regards, Marin Bratanov

### Response

**const** answered on 18 Jun 2020

that works for my purpose, thanks a lot!
