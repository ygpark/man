# PostgreSQL


## 1. 설치

...

## 2. COMMAND LINE

명령행 진입

```
    sudo -u postgres psql
```

## 3. GUI MODE

```
    pgadmin3
```


## 4. XML Query 튜토리얼

### 4.1. OVERVIEW

간단한 형태의 XML 데이터를 넣고 검색한다.

    ```
    <facebook>
        <person>
            <name>Tom</name>
        </person>
        <person>
            <name>Jay</name>
        </person>
    </facebook>
    ```

### 4.2. CREATE TABLE

    ```
    CREATE TABLE xml_table(id serial primary key, xdata xml);
    ```


### 4.3. INSERT

    ```
    INSERT INTO xml_table(xdata) VALUES ('<facebook><person id="1"><name>Tom</name></person><person id="2"><name>Jay</name></person></facebook>');
    INSERT INTO xml_table(xdata) VALUES ('<facebook><person id="3"><name>Linus</name></person><person id="4"><name>Roi</name></person></facebook>');
    ```


### 4.4. SELECT


#### 4.4.1. xpath로 첫번째 name의 값을 갖고오기.

xpath로 갖고오는 데이터는 배열형태다.

첫번째 name의 값을 검색

    ```
    SELECT (xpath('//person/name/text()', xdata)) [1] from xml_table;
    -------
     Tom
     Linus
    (2 rows)
    ```

첫번째 name의 값을 검색, 단 person의 id속성이 1인 것만. (2행이 검색된 것에 주의)

    ```
    SELECT (xpath('//person[@id=1]/name/text()', xdata)) [1] from xml_table;
    -------
     Tom

    (2 rows)
    ```


#### 4.4.2. xpath와 where절로 레코드 선택하기

첫번째 person/name의 값이 Tom인 행을 검색

    ```
    SELECT *
    FROM xml_table
    WHERE (xpath('//person/name/text()', xdata))[1]::text = 'Tom';

     id |                                                 xdata
    ----+-------------------------------------------------------------------------------------------------------
      6 | <facebook><person id="1"><name>Tom</name></person><person id="2"><name>Jay</name></person></facebook>
    (1 row)
    ```

첫번째 person/name의 값이 Tom인 행을 검색

    ```
    SELECT *
    FROM xml_table
    WHERE (xpath('//person/name/text()', xdata))[2]::text = 'Jay';

     id |                                                 xdata
    ----+-------------------------------------------------------------------------------------------------------
      6 | <facebook><person id="1"><name>Tom</name></person><person id="2"><name>Jay</name></person></facebook>
    (1 row)
    ```
#### 4.4.3. [4.4.1], [4.4.2]를 섞은 형태

    ```
    SELECT (xpath('//person/name/text()', xdata)) [1]
    FROM xml_table
    WHERE (xpath('//person/name/text()', xdata))[1]::text = 'Tom';
    -------
     Tom
    (1 row)
    ```

#### 4.4.4. [4.4.3]에서 xml을 가져오는 형태

    ```
    SELECT (xpath('//person[@id=1]', xdata)) [1]
    FROM xml_table
    WHERE (xpath('//person/name/text()', xdata))[1]::text = 'Tom';

    --------------------
     <person id="1">   +
       <name>Tom</name>+
     </person>
    (1 row)
    ```

