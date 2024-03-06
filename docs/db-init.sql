create table items
(
    id                 uuid    default uuid_generate_v4() not null
        constraint items_pk
            primary key,
    application_id     varchar(100),
    dataset_id         varchar(100)                       not null,
    content            text,
    content_normalized text,
    entity_id          varchar(100),
    data               json,
    processed          boolean default false              not null,
    constraint items_ux_application_id_data_set_id_entity_id
        unique (application_id, dataset_id, entity_id)
);

alter table items
    owner to postgres;




create table items_chunks
(
    id                 uuid default uuid_generate_v4() not null
        constraint items_chunks_pk
            primary key,
    item_id            uuid
        constraint items_chunks_items_id_fk
            references items
            on update cascade on delete cascade,
    no                 integer,
    content_normalized text
);

alter table items_chunks
    owner to postgres;




