# Column Sort by Different Value

## Question

**Dus** asked on 18 Dec 2019

Is there any way to sort a column by a different value than what is shown in the grid? I have a grid that lists blobs and their file sizes as a string to include KB, MB, and so on. I'd like to be able to sort the column based on file size, but with the data being a string it doesn't sort correctly. I'd like to have the value represented as an int in bytes, but continue to display the column as a string. Is this possible? Thanks in advance!!

## Answer

**Marin Bratanov** answered on 19 Dec 2019

Hi Dustin, You can use a cell template for this The Field of the column will point to the Size field that you want to sort by, but in the template you will render the string you want your users to see. You can find an example of this here: [https://feedback.telerik.com/blazor/1427060-adding-sortfield-to-grid.](https://feedback.telerik.com/blazor/1427060-adding-sortfield-to-grid.) While this feature implementation has been declined at the moment because it is doable with a template, you can comment and vote on it and if it gains sufficient traction with the community, we could reopen it. Regards, Marin Bratanov

### Response

**Dustin** answered on 19 Dec 2019

I really appreciate how quick you respond to posts! Thank you for the reference!
