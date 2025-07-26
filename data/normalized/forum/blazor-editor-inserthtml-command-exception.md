# Blazor Editor insertHTML command Exception

## Question

**Dav** asked on 29 Mar 2022

Please see REPL: [https://blazorrepl.telerik.com/wcYncXGa24oOJuTr39](https://blazorrepl.telerik.com/wcYncXGa24oOJuTr39) or attached sample file. await Editor.ExecuteAsync( new HtmlCommandArgs( "insertHTML", "Hello", true )); Executing the above code by clicking the Insert button in the REPL throws this exception: Unhandled exception rendering component: _V[e] is not a function TypeError: _V[e] is not a function ... Any workarounds? Thanks!

## Answer

**Dimo** answered on 31 Mar 2022

Hi David, Change the code as follows. Also, please notify us if you submit identical forum thread and a ticket. Thanks. await Editor.ExecuteAsync( new HtmlCommandArgs( " insertHtml ", "Hello", true )); Regards, Dimo Progress Telerik

### Response

**David Tosi** commented on 31 Mar 2022

That fixed it! Thanks for updating the docs too.
