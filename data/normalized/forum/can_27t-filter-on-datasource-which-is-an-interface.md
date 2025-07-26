# Can't filter on DataSource which is an Interface?

## Question

**Jef** asked on 04 Sep 2019

I am passing a collection of an Interface type as the datasource for a the Grid and when I try to render the page I get thr following error... Unhandled exception rendering component: Cannot create an instance of an interface. System.MissingMethodException: Cannot create an instance of an interface. at System.RuntimeTypeHandle.CreateInstance(RuntimeType type, Boolean publicOnly, Boolean wrapExceptions, Boolean& canBeCached, RuntimeMethodHandleInternal& ctor, Boolean& hasNoDefaultCtor) at System.RuntimeType.CreateInstanceDefaultCtorSlow(Boolean publicOnly, Boolean wrapExceptions, Boolean fillCache) at System.RuntimeType.CreateInstanceDefaultCtor(Boolean publicOnly, Boolean skipCheckThis, Boolean fillCache, Boolean wrapExceptions) at System.Activator.CreateInstance[T]() at Telerik.Blazor.Components.Grid.GridFilterHeaderBase`1.get_PropType() I do not know the datasource actual concrete type until run time. Is there a way to work around this? Thanks, Jeff

## Answer

**Marin Bratanov** answered on 05 Sep 2019

Hello Jeff, The grid needs a class that can be instantiated. Interfaces and enums can't, and so can't be used as data sources. Regards, Marin Bratanov

### Response

**Jeff** answered on 05 Sep 2019

If the grid isn't editable then why can't the datasource be an interface? Why does enable filtering require the instantiation of the type? Thanks, Jeff

### Response

**Marin Bratanov** answered on 06 Sep 2019

Hi Jeff, That's the way it is done at the moment. I am not sure if the create calls for the models can be avoided even for a non-editable, non-filterable, non-sortable, non-groupable, non-pageable grid, because I am fairly sure they are needed to extract the types, default values and actual values of the data so it can be rendered. Regards, Marin Bratanov

### Response

**Jeff** answered on 06 Sep 2019

The grid works fine using interfaces if it’s not editable. And sorting works. But turning filtering breaks it. Just for reference the Syncfusion Blazor Grid lets me provide a separate model type from the type of the data source. Then I can create a dummy type that has properties that match the interface and supply that as a type that can be instant Kate’s when necessary. But the Syncfusion grid only needs that in editable mode and for templates. Sorting and filtering work fine with just the interfaces. I like the fact that you are writing your components from scratch in C#. Where as Syncfusion is wrapping their existing is components. Your components are more performant and look nicer but are not as flexible in these types of situations. Thanks, Jeff

### Response

**Marin Bratanov** answered on 09 Sep 2019

Hello Jeff, It seems instantiation of objects is done in different ways in our grid and in theirs. I suspect that for most cases they serialize to a JSON literal for their underlying jQuery widgets and work less with the actual .NET objects, which lets and interface go a longer way. We do believe that going native is the better solution, though, and that may make things seem to get out slower, because we need to write everything from scratch, there isn't anything we wrap or reuse. Regards, Marin Bratanov
