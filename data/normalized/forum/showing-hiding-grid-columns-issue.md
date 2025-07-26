# Showing/Hiding Grid Columns Issue

## Question

**Jos** asked on 15 May 2020

Hello, I've replicated the show/hide grid columns feature as per the grid demo. The only issue i'm having is that "showing" the column results in the column being moved to the end of the grid instead of appearing in the order in which i have it placed in my list of GridColumns. Is this expected behavior and is there a way to force the columns to stay in the defined order even when they are being hidden and shown? Thank You Josh F.

## Answer

**Marin Bratanov** answered on 15 May 2020

Hi Josh, You can follow the implementation of a feature that will allow the column order to be "maintained" in this page: [https://feedback.telerik.com/blazor/1434835-preserve-column-order-when-showing-hiding-columns-dynamically](https://feedback.telerik.com/blazor/1434835-preserve-column-order-when-showing-hiding-columns-dynamically) - you can find the column chooser workaround linked from my last post there. I've also added your Vote to this request to raise its priority. Regards, Marin Bratanov

### Response

**Joshua** answered on 15 May 2020

Marin, Thank you for the quick response. I did see that post and don't quite understand how it differs from the code i have. Am i correct in that it is as simple as by generating the GridColums in a foreach loop, that forces the grid to build the column order from scratch each time? if so then I'm good to go. Thanks Josh F

### Response

**Marin Bratanov** answered on 15 May 2020

Hi Josh, That's what it does - there is one grid that populates a collection of column descriptors. Then, that collection is used to create the actual grid columns. Changing that collection from the first grid causes Blazor to re-render everything in the loop and so the columns have the order they have in the collection. Regards, Marin Bratanov

### Response

**Jim** answered on 02 Sep 2020

Are you guys going to create a GridColumnHidden or an attribute on GridColumn so it is hidden?

### Response

**Marin Bratanov** answered on 03 Sep 2020

Hi Jim, The column will get a Visible parameter that toggles whether it renders or not. It will be available in the upcoming 2.17.0 release (planned for mid-September). Regards, Marin Bratanov

### Response

**Jim** answered on 03 Sep 2020

Will the column still exist in memory so we can read from it?

### Response

**Marin Bratanov** answered on 03 Sep 2020

That depends on what you mean by that. The column component should not be created and rendered in the HTML output, but the data is still in the view-model so you can use it in the logic. Regards, Marin Bratanov

### Response

**Jim** answered on 03 Sep 2020

Say you have a list of key/value pairs. You set that up to display in a grid; except, you don't want to display the Key. When you edit the displayed value, it comes to you in the GridCommandEventArgs in its edited state. So, if the value is edited, how do I locate which of the key/value pairs in the Data that it belongs to - if I can't get to the Key associated with the edit?

### Response

**Jim** answered on 03 Sep 2020

I got the answer. The args.Item is the complete record; so, I just cast it and pull the Id that I need. Thanks.
