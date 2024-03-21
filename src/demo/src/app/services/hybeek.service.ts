import { Injectable } from '@angular/core';
import {DataModel} from "src/app/models/data.model";
import {HttpClient} from "@angular/common/http";
import {SearchResultModel} from "src/app/models/search-result.model";

@Injectable({
  providedIn: 'root'
})
export class HybeekService {

  hybeekApiUrl = "http://127.0.0.1:8000";

  constructor(private http: HttpClient) { }

   AddOrUpdate(item: DataModel)
  {
     return   this.http.post(this.hybeekApiUrl + "/items", item);

  }

    search(applicationId: string, dataSetId: string,    searchText: string, top: number)
    {
        return this.http.get<Array<SearchResultModel>>(this.hybeekApiUrl + "/search?application_id=" + applicationId + "&dataset_id=" + dataSetId + "&search_expression=" + searchText + "&top=" + top);
    }



}
