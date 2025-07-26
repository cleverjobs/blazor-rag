# Published .NET 8 Blazor WASM app throws serialization error Unhandled exception rendering component: ConstructorContainsNullParameterNames

## Question

**Chl** asked on 17 Aug 2023

Hello=====Telerik EDIT: Please update to version 5.0.1 or scroll down to this post with a summary of the problem.=====I'm trying to use latest Telerik Blazor 4.4.0 with dotnet 8.0preview7 Everything is looking ok on Debug side but after building and publishing project to IIS I get an error from rendering any gauge chart (I tried Arc and Radial) Debug: IIS: Log from DevTools crit: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: ConstructorContainsNullParameterNames, System.Collections.Generic.KeyValuePair`2[System.String,System.String] System.NotSupportedException: ConstructorContainsNullParameterNames, System.Collections.Generic.KeyValuePair`2[System.String,System.String] at System.Text.Json.ThrowHelper.ThrowNotSupportedException_ConstructorContainsNullParameterNames(Type ) at System.Text.Json.Serialization.Metadata.DefaultJsonTypeInfoResolver.PopulateParameterInfoValues(JsonTypeInfo ) at System.Text.Json.Serialization.Metadata.DefaultJsonTypeInfoResolver.CreateTypeInfoCore(Type , JsonConverter , JsonSerializerOptions ) at System.Text.Json.Serialization.Metadata.DefaultJsonTypeInfoResolver.CreateJsonTypeInfo(Type , JsonSerializerOptions ) at System.Text.Json.Serialization.Metadata.DefaultJsonTypeInfoResolver.GetTypeInfo(Type , JsonSerializerOptions ) at System.Text.Json.JsonSerializerOptions.GetTypeInfoNoCaching(Type ) at System.Text.Json.JsonSerializerOptions.CachingContext.CreateCacheEntry(Type type, CachingContext context) --- End of stack trace from previous location --- at System.Text.Json.JsonSerializerOptions.CachingContext.CacheEntry.GetResult() at System.Text.Json.JsonSerializerOptions.CachingContext.GetOrAddTypeInfo(Type , Boolean ) at System.Text.Json.JsonSerializerOptions.GetTypeInfoInternal(Type , Boolean , Nullable`1 , Boolean , Boolean ) at System.Text.Json.Serialization.Metadata.JsonTypeInfo.Configure() at System.Text.Json.Serialization.Metadata.JsonTypeInfo.<EnsureConfigured>g__ConfigureSynchronized|170_0() at System.Text.Json.Serialization.Metadata.JsonTypeInfo.EnsureConfigured() at System.Text.Json.JsonSerializerOptions.GetTypeInfoInternal(Type , Boolean , Nullable`1 , Boolean , Boolean ) at System.Text.Json.JsonSerializerOptions.GetTypeInfoForRootType(Type , Boolean ) at System.Text.Json.JsonSerializerOptions.TryGetPolymorphicTypeInfoForRootType(Object , JsonTypeInfo& ) at System.Text.Json.Serialization.Metadata.JsonTypeInfo`1[[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].Serialize(Utf8JsonWriter , Object& , Object ) at System.Text.Json.JsonSerializer.WriteString[Object](Object& , JsonTypeInfo`1 ) at System.Text.Json.JsonSerializer.Serialize[Object](Object value, JsonSerializerOptions options) at Telerik.Blazor.Common.Serialization.DefaultJavaScriptSerializer.Serialize(Object value) at Telerik.Blazor.Common.Serialization.JavaScriptInitializer.Serialize(IDictionary`2 object) at Telerik.Blazor.Common.Serialization.JavaScriptInitializer.Serialize(IDictionary`2 object) at Telerik.Blazor.Common.Serialization.JavaScriptInitializer.Serialize(IDictionary`2 object) at Telerik.Blazor.Common.Serialization.JavaScriptInitializer.Serialize(IDictionary`2 object) at Telerik.Blazor.Common.Serialization.JavaScriptInitializer.Serialize(IDictionary`2 object) at Telerik.Generated.Blazor.Components.DataVizComponent.Serialize(IJavaScriptInitializer serializer) at Telerik.Generated.Blazor.Components.DataVizComponent.Serialize() at Telerik.Generated.Blazor.Components.DataVizComponent.InitOrUpdateWidget() at Telerik.Generated.Blazor.Components.DataVizComponent.OnAfterRender(Boolean firstRender) at Telerik.Blazor.Components.TelerikRadialGauge.OnAfterRender(Boolean firstRender) at Microsoft.AspNetCore.Components.ComponentBase.Microsoft.AspNetCore.Components.IHandleAfterRender.OnAfterRenderAsync() at Microsoft.AspNetCore.Components.Rendering.ComponentState.NotifyRenderCompletedAsync() Thanks for reply

### Response

**Dimo** commented on 22 Aug 2023

Chladek - hm, we haven't observed this error ever before. Perhaps this discussion will help? In general, our Charts and Gauges serialize their data for client-side rendering. The components will honor any server-side serialization settings, so this may create unwanted side effects.

### Response

**Chladek** commented on 24 Aug 2023

Hello Dimo, I did not include the gauges in final release but I will come back to this at new update which was listed to be in late August. I hope it will be fixed in that. It looks the problem is between new version of System.Text.Json and Gauge ( Announcing .NET 8 Preview 7 - .NET Blog (microsoft.com) )

### Response

**Dimo** commented on 24 Aug 2023

Thanks for the update, Chladek. I forwarded this to our devs to be aware of the potential issue.

### Response

**ben** commented on 29 Aug 2023

I'm seeing the same behavior with Telerik Blazor 4.4.0 and .net70. Works great in debug mode, starts to throw the same exception in release on IIS. In this case I'm playing with TelerikChart and RenderAs="@RenderingMode.Canvas" Is there a work around documented?

### Response

**Dimo** commented on 31 Aug 2023

@Ben - I created a new .NET 7 Blazor Server App with a Chart inside. I published it to my local IIS and it worked as expected. So perhaps there is some other problem. I am attaching the app for your reference.

### Response

**ben** commented on 31 Aug 2023

@Dimo, Blazor Wasm, not Blazor Server. Additionally configured to use Newtonsoft and not System.Text.Json Json serialization in the Server and Web project

### Response

**Chladek** commented on 31 Aug 2023

@Dimo I've updated Telerik to 4.5.0 but issue is still there @ben Yes I'm using Blazor Wasm too

### Response

**Dimo** commented on 31 Aug 2023

Server vs WebAssembly is hardly an issue here. Newtonsoft.Json is known to cause problems with our components in specific scenarios. Generally, we recommend System.Text.Json instead. Have you seen these articles? They provide some tips and workarounds. [https://docs.telerik.com/blazor-ui/knowledge-base/chart-newtonsoft-seialization-settings](https://docs.telerik.com/blazor-ui/knowledge-base/chart-newtonsoft-seialization-settings) [https://docs.telerik.com/blazor-ui/knowledge-base/common-newtonsoft-breaks-datasourcerequest-serialization](https://docs.telerik.com/blazor-ui/knowledge-base/common-newtonsoft-breaks-datasourcerequest-serialization) - see Solution and Workarounds

### Response

**ben** commented on 31 Aug 2023

@Dimo you have an example where this is working for Blazor Wasm after publish in Release to IIS? It appears something is getting stripped out during the .net publish

### Response

**Dimo** commented on 05 Sep 2023

@Ben - please check the attached solution. I published it to IIS and it worked as expected.

### Response

**Chladek** commented on 20 Oct 2023

Hi @Dimo Sorry for late reply but after some research I think it is problem with trimming in Telerik I've got same error even in DatePicker even in 2 different projects -> both are in .net8rc2 right now See included error Thanks for reply Unhandled exception rendering component: ConstructorContainsNullParameterNames, System.Collections.Generic.KeyValuePair`2[System.String,System.String] SerializationNotSupportedParentType, System.Object Path: $.
System.NotSupportedException: ConstructorContainsNullParameterNames, System.Collections.Generic.KeyValuePair`2[System.String,System.String] SerializationNotSupportedParentType, System.Object Path: $.
---> System.NotSupportedException: ConstructorContainsNullParameterNames, System.Collections.Generic.KeyValuePair`2[System.String,System.String]
at System.Text.Json.ThrowHelper.ThrowNotSupportedException_ConstructorContainsNullParameterNames(Type )
at System.Text.Json.Serialization.Metadata.DefaultJsonTypeInfoResolver.PopulateParameterInfoValues(JsonTypeInfo )
at System.Text.Json.Serialization.Metadata.DefaultJsonTypeInfoResolver.CreateTypeInfoCore(Type , JsonConverter , JsonSerializerOptions )
at System.Text.Json.Serialization.Metadata.DefaultJsonTypeInfoResolver.CreateJsonTypeInfo(Type , JsonSerializerOptions )
at System.Text.Json.Serialization.Metadata.DefaultJsonTypeInfoResolver.GetTypeInfo(Type , JsonSerializerOptions )
at System.Text.Json.JsonSerializerOptions.GetTypeInfoNoCaching(Type )
at System.Text.Json.JsonSerializerOptions.CachingContext.CreateCacheEntry(Type type, CachingContext context)
--- End of stack trace from previous location ---
at System.Text.Json.JsonSerializerOptions.CachingContext.CacheEntry.GetResult()
at System.Text.Json.JsonSerializerOptions.CachingContext.GetOrAddTypeInfo(Type , Boolean )
at System.Text.Json.JsonSerializerOptions.GetTypeInfoInternal(Type , Boolean , Nullable`1 , Boolean , Boolean )
at System.Text.Json.Serialization.Metadata.JsonTypeInfo.Configure()
at System.Text.Json.Serialization.Metadata.JsonTypeInfo.<EnsureConfigured>g__ConfigureSynchronized|170_0()
at System.Text.Json.Serialization.Metadata.JsonTypeInfo.EnsureConfigured()
at System.Text.Json.JsonSerializerOptions.GetTypeInfoInternal(Type , Boolean , Nullable`1 , Boolean , Boolean )
at System.Text.Json.WriteStackFrame.InitializePolymorphicReEntry(Type , JsonSerializerOptions )
at System.Text.Json.Serialization.JsonConverter.ResolvePolymorphicConverter(Object , JsonTypeInfo , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWrite(Utf8JsonWriter , Object& , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.Converters.DictionaryOfTKeyTValueConverter`3[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].OnWriteResume(Utf8JsonWriter , Dictionary`2 , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonDictionaryConverter`3[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].OnTryWrite(Utf8JsonWriter , Dictionary`2 , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWrite(Utf8JsonWriter , Dictionary`2& , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWriteAsObject(Utf8JsonWriter , Object , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWrite(Utf8JsonWriter , Object& , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.Converters.DictionaryOfTKeyTValueConverter`3[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].OnWriteResume(Utf8JsonWriter , Dictionary`2 , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonDictionaryConverter`3[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].OnTryWrite(Utf8JsonWriter , Dictionary`2 , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWrite(Utf8JsonWriter , Dictionary`2& , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWriteAsObject(Utf8JsonWriter , Object , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWrite(Utf8JsonWriter , Object& , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.Converters.DictionaryOfTKeyTValueConverter`3[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].OnWriteResume(Utf8JsonWriter , Dictionary`2 , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonDictionaryConverter`3[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].OnTryWrite(Utf8JsonWriter , Dictionary`2 , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWrite(Utf8JsonWriter , Dictionary`2& , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWriteAsObject(Utf8JsonWriter , Object , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWrite(Utf8JsonWriter , Object& , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.Converters.DictionaryOfTKeyTValueConverter`3[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].OnWriteResume(Utf8JsonWriter , Dictionary`2 , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonDictionaryConverter`3[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].OnTryWrite(Utf8JsonWriter , Dictionary`2 , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWrite(Utf8JsonWriter , Dictionary`2& , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWriteAsObject(Utf8JsonWriter , Object , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWrite(Utf8JsonWriter , Object& , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.Converters.DictionaryOfTKeyTValueConverter`3[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].OnWriteResume(Utf8JsonWriter , Dictionary`2 , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonDictionaryConverter`3[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].OnTryWrite(Utf8JsonWriter , Dictionary`2 , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWrite(Utf8JsonWriter , Dictionary`2& , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWriteAsObject(Utf8JsonWriter , Object , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWrite(Utf8JsonWriter , Object& , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.Converters.ArrayConverter`2[[System.Object[], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].OnWriteResume(Utf8JsonWriter , Object[] , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonCollectionConverter`2[[System.Object[], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].OnTryWrite(Utf8JsonWriter , Object[] , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Object[], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].TryWrite(Utf8JsonWriter , Object[]& , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.JsonConverter`1[[System.Object[], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].WriteCore(Utf8JsonWriter , Object[]& , JsonSerializerOptions , WriteStack& )
Exception_EndOfInnerExceptionStack
at System.Text.Json.ThrowHelper.ThrowNotSupportedException(WriteStack& , NotSupportedException )
at System.Text.Json.Serialization.JsonConverter`1[[System.Object[], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].WriteCore(Utf8JsonWriter , Object[]& , JsonSerializerOptions , WriteStack& )
at System.Text.Json.Serialization.Metadata.JsonTypeInfo`1[[System.Object[], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].Serialize(Utf8JsonWriter , Object[]& , Object )
at System.Text.Json.JsonSerializer.WriteString[Object[]](Object[]& , JsonTypeInfo`1 )
at System.Text.Json.JsonSerializer.Serialize[Object[]](Object[] , JsonSerializerOptions )
at Microsoft.JSInterop.JSRuntime.InvokeAsync[Object](Int64 , String , CancellationToken , Object[] )
at Microsoft.JSInterop.JSRuntime.<InvokeAsync>d__16`1[[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext()
at Telerik.Blazor.Components.Common.DateInputs.DateInput`1.<OnAfterRenderAsync>d__186[[System.Nullable`1[[System.DateTime, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext()

### Response

**Dimo** commented on 23 Oct 2023

Hi Chladek, Can you provide a simple and runnable project, which reproduces this problem? I am not able to observe it with the .NET 8 test apps that I have.

### Response

**Matt** commented on 15 Nov 2023

@Dimo, I was hoping this would be fixed with the official release of .NET 8 and Telerik UI for Blazor 5.0.0 but the problem still exists. I have attached the application you had attached just modified a bit. I updated it to .NET 8 and updated package references. Everything works fine with running it locally but once you publish it, that same error is shown. I also added a DatePicker as @Chladek had done to the Counter page and it also throws an error. You can just publish it to a local folder and run it and that error is thrown. This makes using .NET 8 unusable with Telerik Blazor.

### Response

**Tuomas** commented on 20 Nov 2023

Same problem also. We have WASM app, .NET 8 and Telerik UI for Blazor 5.0.0. DatePicker is throwing an error. Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: ConstructorContainsNullParameterNames, System.Collections.Generic.KeyValuePair`2[System.String,System.String] SerializationNotSupportedParentType, System.Object Path: $. System.NotSupportedException: ConstructorContainsNullParameterNames, System.Collections.Generic.KeyValuePair`2[System.String,System.String] SerializationNotSupportedParentType, System.Object Path: $. ---> System.NotSupportedException: ConstructorContainsNullParameterNames, System.Collections.Generic.KeyValuePair`2[System.String,System.String] ...... at System.Text.Json.JsonSerializer.Serialize[Object[]](Object[] , JsonSerializerOptions )
at Microsoft.JSInterop.JSRuntime.InvokeAsync[Object](Int64 , String , CancellationToken , Object[] )
at Microsoft.JSInterop.JSRuntime. <InvokeAsync> d__16`1[[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext()
at Telerik.Blazor.Components.Common.DateInputs.DateInput`1. <OnAfterRenderAsync> d__199[[System.Nullable`1[[System.DateTime, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext() I hope that you get this fixed soon.

## Answer

**Dimo** answered on 16 Nov 2023

Hello everyone, We managed to observe and get better understanding about the discussed problem. Here is what we can share: As you correctly assumed, the exception is related to trimming. The specific trigger is serialization of KeyValuePairs. We reproduced the problem without our components. Here is the logged issue on the dotnet repository. We have released a patch version 5.0.1 of Telerik UI for Blazor with a workaround. Another possible workaround for you is to configure granular trimming and ensure the all required assemblies are not trimmed. For example: <Target Name="EnsureAllAssembliesAreLinked" BeforeTargets="PrepareForILLink"> <ItemGroup> <TrimmerRootAssembly Include="System.Private.CoreLib" /> <TrimmerRootAssembly Include="System.Private.Uri" /> <TrimmerRootAssembly Include="System.Runtime" /> <TrimmerRootAssembly Include="System.Runtime.InteropServices" /> <TrimmerRootAssembly Include="System.Threading" /> <TrimmerRootAssembly Include="System.Threading.Tasks.Extensions" /> <TrimmerRootAssembly Include="System.Memory" /> <TrimmerRootAssembly Include="System.Console" /> <TrimmerRootAssembly Include="System.Collections" /> <TrimmerRootAssembly Include="System.ObjectModel" /> <TrimmerRootAssembly Include="System.Linq" /> <TrimmerRootAssembly Include="System.Linq.Queryable" /> <TrimmerRootAssembly Include="System.Reflection.Emit" /> <TrimmerRootAssembly Include="System.Linq.Expressions" /> <TrimmerRootAssembly Include="System.Net.Primitives" /> <TrimmerRootAssembly Include="System.Diagnostics.DiagnosticSource" /> <TrimmerRootAssembly Include="System.Net.Security" /> <TrimmerRootAssembly Include="System.Net.Http" /> <TrimmerRootAssembly Include="System.Text.Json" /> <TrimmerRootAssembly Include="System.Net.Http.Json" /> <TrimmerRootAssembly Include="System.ComponentModel.TypeConverter" /> <TrimmerRootAssembly Include="System.Collections.Concurrent" /> <TrimmerRootAssembly Include="System.ComponentModel.Primitives" /> <TrimmerRootAssembly Include="System.Text.RegularExpressions" /> <TrimmerRootAssembly Include="System.ComponentModel" /> <TrimmerRootAssembly Include="System.ComponentModel.Annotations" /> <TrimmerRootAssembly Include="System.Runtime.Numerics" /> <TrimmerRootAssembly Include="System.Collections.NonGeneric" /> <TrimmerRootAssembly Include="System.Runtime.Serialization" /> <TrimmerRootAssembly Include="System.Runtime.Serialization.Xml" /> <TrimmerRootAssembly Include="System.Runtime.Serialization.Primitives" /> <TrimmerRootAssembly Include="System.Runtime.Serialization.Json" /> <TrimmerRootAssembly Include="System.Runtime.Serialization.Formatters" /> <TrimmerRootAssembly Include="System.Data.Common" /> <TrimmerRootAssembly Include="netstandard" /> <TrimmerRootAssembly Include="Microsoft.AspNetCore.Components" /> <TrimmerRootAssembly Include="Microsoft.Extensions.DependencyInjection.Abstractions" /> <TrimmerRootAssembly Include="Microsoft.JSInterop" /> <TrimmerRootAssembly Include="Microsoft.AspNetCore.Components.Forms" /> <TrimmerRootAssembly Include="Microsoft.AspNetCore.Components.Web" /> <TrimmerRootAssembly Include="Microsoft.Extensions.Logging.Abstractions" /> <TrimmerRootAssembly Include="System.Text.Encodings.Web" /> <TrimmerRootAssembly Include="System.Runtime.Loader" /> <TrimmerRootAssembly Include="Microsoft.JSInterop.WebAssembly" /> <TrimmerRootAssembly Include="Microsoft.Extensions.Logging" /> <TrimmerRootAssembly Include="Microsoft.Extensions.Configuration.Abstractions" /> <TrimmerRootAssembly Include="Microsoft.Extensions.Configuration.Json" /> <TrimmerRootAssembly Include="Microsoft.Extensions.Configuration" /> <TrimmerRootAssembly Include="Microsoft.Extensions.Primitives" /> <TrimmerRootAssembly Include="Microsoft.Extensions.DependencyInjection" /> <TrimmerRootAssembly Include="Microsoft.AspNetCore.Components.WebAssembly" /> <TrimmerRootAssembly Include="System.Diagnostics.TraceSource" /> <TrimmerRootAssembly Include="System.Text.Encoding.Extensions" /> <TrimmerRootAssembly Include="System.Collections.Specialized" /> <TrimmerRootAssembly Include="System.Threading.Thread" /> </ItemGroup> </Target> ( @Matt, thanks for preparing a sample for us.) Regards, Dimo Progress Telerik

### Response

**Graham** commented on 16 Nov 2023

I get this problem when publishing but I have the "Trim Unused Code" checkbox unchecked!

### Response

**paul** commented on 28 Nov 2023

Indeed, in the wasm project file, adding <PublishTrimmed>false</PublishTrimmed> fixes the problem.

### Response

**Matias** commented on 04 Dec 2023

Hi @Dimo, We are still experiencing the same error in the published version of the WASM app when we publish with Release configuration. It's working when publishing with Debug configuration. Already updated Telerik version to 5.0.1, and also added the configuration which you have provided to the project file. Tried to disable trimming with <PublishTrimmed>false</PublishTrimmed> as well without any luck. Our publish settings:

### Response

**Dimo** commented on 06 Dec 2023

@Matias - can you provide a small project that reproduces the problem? We are no longer able to observe it with version 5.0.1. Perhaps there is some specific scenario (component configuration) that we haven't used.

### Response

**Matias** commented on 06 Dec 2023

@Dimo, I managed to reproduce this with the following details. Please confirm whether this is reproducible at your side as well or not. - Using TelerikDatePicker component - Value property is null (which is valid according to its docs and it was worked before .NET 8) - Deployed version (Release configuration) with .NET 8 Please confirm whether this will be fixed or not in the near future. Thanks.

### Response

**Dimo** commented on 07 Dec 2023

@Matias I am attaching my .NET 8 test app and here is a video: [https://app.screencast.com/XHC7R6n5X66Ob](https://app.screencast.com/XHC7R6n5X66Ob) After making the video, I noticed that I forgot to demonstrate all publish settings. I can't use win-x86, so I tested with Portable and win-x64. " Remove additional files at destination " was checked in both cases.

### Response

**Matias** commented on 14 Dec 2023

Thanks for your help. Finally it turned out that we needed to delete all contents of obj and bin folders of the WASM project, and then do the publish... Clearing the project from VS, and clearing the publish target was not enough.

### Response

**Dimo** commented on 14 Dec 2023

I see. Thanks for the follow-up!
