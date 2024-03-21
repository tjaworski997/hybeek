import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import {FormsModule} from "@angular/forms";
import {DataModel} from "src/app/models/data.model";
import {HybeekService} from "src/app/services/hybeek.service";
import {lastValueFrom} from "rxjs";
import {SearchResultModel} from "src/app/models/search-result.model";


@Component({
  selector: 'app-root',
  standalone: true,
    imports: [CommonModule, RouterOutlet, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {

  applicationId="ex7";
  dataSetId = "team"
  data = "";
  searchText = "";
  result: Array<SearchResultModel> = [];

  constructor(private  hybeekService: HybeekService) {}


  async importData() {

      const data: Array<DataModel> = [];
      const lines = this.data.split("\n");

      lines.forEach(line => {
          const parts = line.split(". ");
          data.push(
              {
                  application_id: this.applicationId,
                  dataset_id: this.dataSetId,
                  entity_id: parts[0],
                  content: parts[1],
                  data: {text: parts[1]}
              });
      });

      console.log("Data to add or update:", data);

      for(const item of data) {
          console.log("Adding or updating item: ", item);
          const res$ =  this.hybeekService.AddOrUpdate(item);
          const res = await lastValueFrom(res$)
          console.log("Response: ", res);
      };
  }

    search() {
      console.log("Searching for: ", this.searchText);


      const res$ = this.hybeekService.search(this.applicationId, this.dataSetId, this.searchText, 3);
        lastValueFrom(res$).then(res => {
            console.log("Search result: ", res);
            this.result = res;
        });


    }

    protected readonly JSON = JSON;
}
