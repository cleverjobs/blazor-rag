# Grid Column AutoSize When DetailTemplate Shown Only Using Headers

## Question

**Joh** asked on 24 Mar 2025

I discovered an issue with auto-sizing grid columns with a DetailTemplate, but it depends on if the DetailTemplate is displayed or not. It seems that when the DetailTemplate is not shown, the AutoSize works as expected, but when the DetailTemplate is shown the AutoSIze seems to size to the column header only. In addition, the top table has a column with an unspecified width so it will fill the space to get the table to 100%. I noticed that on AutoSize the total table width and the other column kept their original width. When columns resized larger than they were, this made the overall table too long and scrollable. So after the resize, I used the table state and set the table and column with to null. await grid.AutoFitColumnAsync( "colProjectDetailModuleAmbTemp" ); await grid.AutoFitColumnAsync( "colProjectDetailModuleTitle" ); var st=grid.GetState();
st.ColumnStates.Where(c=> c.Id=="colProjectDetailModuleDesignTypes" ).First().Width=null;
st.TableWidth=null; await grid.SetStateAsync(st); I have attached images for your reference. Is it a bug that the AutoSize is only using the column headers when the DetailTemplate is shown or am I missing something to get it to resize correctly?

## Answer

**Tsvetomir** answered on 27 Mar 2025

Hi Johnathan, The encountered behavior, where Autofit functionality seems to only consider the column headers when a DetailTemplate is displayed, is not the intended functionality. The presence of a DetailTemplate might be affecting the rendering and sizing calculations, leading to this unexpected behavior. With that in mind, I've tried to replicate the behavior on my side within this REPL link. As a result, the columns are resized as expected when the DetailsTemplate is displayed. As a next step, can you please modify the REPL to reproduce the behavior and send it back to me for inspection? This will allow me to see the behavior on my side and troubleshoot further. I look forward to your reply. Regards, Tsvetomir

### Response

**Johnathan** answered on 04 Apr 2025

Sorry I didn't see your response earlier. Before I play with it, can you make the following changes: Make all but one of the columns a fixed width. That way the table and the column will resize with the window. After any autofit, the table and column should still be resizing (as before the autofit). I just want to see if you do it the same way I did and if it is different is my way causing the behavior. Additionally, I have a context menu attached to the rows. I know that causes a re-render, but I don't know if it is the cause.

### Response

**Tsvetomir** commented on 07 Apr 2025

Hello Johnathan, I modified the example as you've recommended; added a specific width to all columns except one. As a result the autofit is still working as expected. I'm attaching a screen recording where I test the behavior with the modified example. Also, sharing the modified REPL example - [https://blazorrepl.telerik.com/QJuSaLEg56IKbHbj39.](https://blazorrepl.telerik.com/QJuSaLEg56IKbHbj39.) Additionally, it doesn't seem the described context menu to have relation to the encountered behavior. However, you can test it on your end by removing the context menu only. With the above in mind, I recommend you to modify the REPL example on you end to reproduce the behavior and send it back to me. On a side note, you can check the Grid Column Width documentation.
