# TreeList - Difference between TreeList.GetState() and TreeList.State

## Question

**TedTed** asked on 10 Jun 2022

Hi, I'm trying to understand if there is any difference between using TreeList.GetState() and TreeList.State? I want to examine the state of the tree list in the most efficient manner possible, and TreeList.State seems like the obvious choice, but the docs all use the GetState() method. Thanks.

## Answer

**Dimo** answered on 15 Jun 2022

Hi Ted, TreeList. State is for internal use only. Always use GetState(). Some of our API members are public, although they should not be used by developers. For example, this includes JsInvokable C# methods and API members that are related to some specific interfaces. If you don't see an API member in our documentation, examples and API reference, it may be for internal use. Regards, Dimo Progress Telerik
