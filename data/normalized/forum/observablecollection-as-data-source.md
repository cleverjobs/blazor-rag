# ObservableCollection as data source

## Question

**Rob** asked on 25 Mar 2021

The following code leads to an infinite loop and call stack exhaustion. How to use the grid with an ObservableCollection as data source? @page "/Test" @using System.Collections.ObjectModel <TelerikGrid Data="_data" Pageable="true" OnRead="@Read" /> @code { private readonly ObservableCollection<object> _data=new(); protected Task Read(GridReadEventArgs args) { Console.WriteLine("Read"); _data.Add(new()); return(Task.FromResult(0)); } }

## Answer

**Marin Bratanov** answered on 29 Mar 2021

Hello Robert, This is documented in the article about the OnRead event: If you are using an ObservableCollection, make sure to create a new one, because using .Add(), .Remove() or .Clear() on it will cause an infinite loop - the grid monitors the ObservableCollection events and updates its data, which will fire OnRead. I've added a note about it in the article on handling Observable data too ( commit link that will be live with our next upload). Regards, Marin Bratanov
