# SearchBox events

## Question

**Bla** asked on 26 Jul 2022

Hello. I have a treelist whose nodes can be expanded or not. I would like that when a search is performed, the resulting nodes are all expanded. In the documentation I can't find events like OnSearch, BeforeSearch, AfterSearch... so that I can change the state of the nodes after a search is performed. Are these SearchBox events accessible. If not, any idea how to achieve my goal? Thank you very much.

### Response

**Blazorist** commented on 26 Jul 2022

I can hook from the OnStateChanged event of the TreeList and filter by PropertyName=="SearchFilter". The truth is that I don't like this solution because this event is called on almost anytime that something happens in the tree. With the currently exposed events, is there a better solution?
