# Metroclima database dumper


This is a simple Python tool to retrieve information from  the Porto Alegre city's Metroclima database, automating the use of the form available at http://www2.portoalegre.rs.gov.br/ceic/default.php?p_secao=52

It posts the given options to the Metroclima web site and returns the URL to download the generated dump file. It's possible to download the file directly.

### Script help

```bash
$ python -m metroclima --help

Usage: metroclima [OPTIONS] COMMAND [ARGS]...

  A simple tool to retrieve information from the Porto Alegre city's
  Metroclima database.

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  get  Retrieve dump from Metroclima site

```

#### GET command help

All arguments have default values thus you can run the command `python -m metroclima get` without further arguments.

```bash
$ python -m metroclima get --help

Usage: metroclima get [OPTIONS]

  Retrieve dump from Metroclima site

Options:
  -f, --filetype [csv|json|xls]   The dump file type
  -y, --year [2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018]
                                  Choose which year
  -q, --quarter [1|2|3|4]         Choose which quarter
  -s, --sensor [TEMPERATURE|SENSATION|HUMIDITY|RAIN|PRESSURE|WIND|DEW]
                                  Choose the type of sensor
  -l, --station [MENINO_DEUS|MOINHOS_DE_VENTO|SERRARIA|SAO_JOAO|LOMBA_DO_PINHEIRO|LAMI|CENTRO_HISTORICO|SARANDI|GLORIA|TRISTEZA]
                                  Choose which station
  -d, --download                  Downloads
  -h, --help                      Show this message and exit.

```

#### Getting the file URL with default arguments
```bash

$ python -m metroclima get
Retrieving download URL...
http://metroclima1.procempa.com.br/downloads/../downloads/MeninoDeus_Temperatura_2018-01-01_2018-03-31.csv

```

#### Getting the file URL and downloading it with default arguments
```bash

$ python -m metroclima get -d
Retrieving download URL...
http://metroclima1.procempa.com.br/downloads/../downloads/MeninoDeus_Temperatura_2018-01-01_2018-03-31.csv
Downloading file...
/home/user/MeninoDeus_Temperatura_2018-01-01_2018-03-31.csv

```

### Downloading many files at once
```bash
$ for sensor in TEMPERATURE SENSATION HUMIDITY RAIN PRESSURE WIND DEW;
>  do  python -m metroclima get -s $sensor -d
> done

Retrieving download URL...
http://metroclima1.procempa.com.br/downloads/../downloads/MeninoDeus_Temperatura_2018-01-01_2018-03-31.csv
Downloading file...
File download at:
/home/user/MeninoDeus_Temperatura_2018-01-01_2018-03-31.csv
Retrieving download URL...
http://metroclima1.procempa.com.br/downloads/../downloads/MeninoDeus_SensacaoTerm_2018-01-01_2018-03-31.csv
Downloading file...
File download at:
/home/user/MeninoDeus_SensacaoTerm_2018-01-01_2018-03-31.csv
Retrieving download URL...
http://metroclima1.procempa.com.br/downloads/../downloads/MeninoDeus_Umidade_2018-01-01_2018-03-31.csv
Downloading file...
File download at:
/home/user/MeninoDeus_Umidade_2018-01-01_2018-03-31.csv
Retrieving download URL...
http://metroclima1.procempa.com.br/downloads/../downloads/MeninoDeus_Chuva_2018-01-01_2018-03-31.csv
Downloading file...
File download at:
/home/user/MeninoDeus_Chuva_2018-01-01_2018-03-31.csv
Retrieving download URL...
http://metroclima1.procempa.com.br/downloads/../downloads/MeninoDeus_Pressao_2018-01-01_2018-03-31.csv
Downloading file...
File download at:
/home/user/MeninoDeus_Pressao_2018-01-01_2018-03-31.csv
Retrieving download URL...
http://metroclima1.procempa.com.br/downloads/../downloads/MeninoDeus_Vento_2018-01-01_2018-03-31.csv
Downloading file...
File download at:
/home/user/MeninoDeus_Vento_2018-01-01_2018-03-31.csv
Retrieving download URL...
http://metroclima1.procempa.com.br/downloads/../downloads/MeninoDeus_Orvalho_2018-01-01_2018-03-31.csv
Downloading file...
File download at:
/home/user/MeninoDeus_Orvalho_2018-01-01_2018-03-31.csv

```