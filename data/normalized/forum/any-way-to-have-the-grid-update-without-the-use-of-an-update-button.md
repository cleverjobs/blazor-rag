# Any way to have the grid update without the use of an Update button?

## Question

**TomTom** asked on 04 Sep 2019

In testing I'm finding users keep forgetting to press the Update button on the grid. Is there any way to make the grid update the data source on each data change and not require the use of the row Update buttons?

## Answer

**Tom** answered on 04 Sep 2019

Scratch that.. I've belatedly realised that although InCell editing mode has an Update button, the user doesn't actually need to press it. Ideally I'd like to not have to show that button at all, and instead have a cancel button, but I appreciate that's not an option at the moment.

### Response

**Marin Bratanov** answered on 05 Sep 2019

Hello Tom, To add a little bit of context - the Update button in InCell editing is needed for new item insertion. Updating existing items happens when their editor changes value (blur or enter). An option you can consider is to use an observable collection to add items so you can remove the Add and Update buttons from the grid. Or, you could keep the Add button, but switch it to a custom command that opens up an external insert form in a fashion similar to this demo. Regards, Marin Bratanov

### Response

**Tom** answered on 05 Sep 2019

Hi Marin The grid now working with Observables and INotifyChanged has sorted out several issues for me, that was a really worthwhile change. Re this point: [quote] Marin Bratanov said: use an observable collection to add items so you can remove the Add and Update buttons from the grid. [/quote] Am I correct to say in that scenario I'd need to add an Add button somewhere else that then added a new row to the observable collection (and the grid would then show that row)? I.e. there's no built-in way to have a new row record at the top or bottom of the list where the user can just start entering a record without pressing an Add button ( like MS Access for example )? I appreciate I could add that 'new' row in the collection and sort the data source in such a way that the 'new' row would be at the top, just double checking what the grid does out of the box.

### Response

**Marin Bratanov** answered on 06 Sep 2019

Hello Tom, The built-in Add button on the grid toolbar puts a row at the top of the grid, but this model is not yet in the data source the grid is bound to. Once the user clicks the Save command column button, you get the Create event, so you can add the new model to the grid data source - you can do that at the end (List<T>.Add(myNewModel)), or at the top (List<T>.Insert(0, myNewModel)). I was under the impression that you didn't want the built-in Add and Save buttons from the grid, which is why I suggested implementing the insertion of a new record separately. You can still invoke it from a button on the grid toolbar, though, just use a command name that is different from "Add" so you can handle it as a custom command that does not invoke the built-in row addition. There must be some form of an Add/Insert New Item button, because the grid can't otherwise know to add this blank row. If I am misunderstanding something or you need some more details, just let me know. Regards, Marin Bratanov
