PlacesApi.placeDetails(apiContext, placeId)
        .region("br")
        .language("pt-BR")
        .fields(*PlaceDetailsRequest.FieldMask.values())
        .await()