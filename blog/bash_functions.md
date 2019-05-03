# Занимательные функции в BASH на macOS

Без лишних предисловий просто расскажу о функциях bash profile, которыми сам пользуюсь.

### Изменение громкости
Для того, чтобы изменить громкость звука в macOS с помощью терминала, добавьте в `~/.profile` (или `~/.bash_profile`, в зависимости от того, что у вас там есть) такую функцию:

```
function vl() {
    osascript -e "set Volume $1"
    }
```

Теперь можно изменять громкость системного звука с помощью команды `vl` и параметра от 0 до 7. Причем можно задавать промежуточные значения, например 3.5 (50% громкости)


### Включение-выключение VPN (IPSec)

Если вы пользуетесь VPN по протоколу IPSec, то с помощью этой функции вы сможете включать и выключать настроенный профиль (предполагается, что профиль VPN уже есть у вас в системе), а также узнать статус подключения. 

```
function uvpn() 
{
    INFO=`scutil --nc list`
    status=$(echo "${INFO}" | awk '{if (NR!=1) print$2}' | sed -e 's/[()]//g')
    vpnName=$(echo "${INFO}" | awk 'BEGIN {ORS=" "}; {if (NR!=1) for(i = 5;i <= NF-1; i++) print$i}' | sed -e 's/"//g')
    vpnID=$(echo "${INFO}" | awk '{if (NR!=1) print$3}')
    
    case "$1" in
        start) echo "started $vpnName"
               scutil --nc $1 $vpnID;;
        stop) echo "stopping $vpnName"
              scutil --nc $1 $vpnID
              status=$(scutil --nc list | awk '{if (NR!=1) print$2}' | sed -e 's/[()]//g')
              sleep .5
              echo VPN is $status;;
        *) echo VPN is $status;;
    esac    
}
```

Запуск `uvpn` без параметров покажет состояние подключения. Соответственно `uvpn start` и `uvpn stop` довольно self-explanatory. К сожалению, если у вас IKEv2 VPN, этот скрипт не поможет. В интернете есть для этого [решение](http://matt.coneybeare.me/how-to-setup-an-auto-reconnect-script-for-an-ikev2-vpn-service-on-your-mac/) с помощью Apple Script, но я его не тестировал.

### Управление охлаждением процессора

Для работы этого скрипта вам понадобится установить программу SMCFanControl. Несмотря на то, что данная улитита старая и проверенная, [разработчик](https://github.com/hholtmann/smcFanControl) напоминает, что программу стоит запускать на свой страх и риск, и что манипуляции с вентиляторами процессора могут привести к выходу компьютера из строя. Короче, я предупредил. 

```
alias smc="/Applications/smcFanControl.app/Contents/Resources/smc"

function fan()
{
    RPM=$2
    FANSTOTAL=$(smc -f | awk  'BEGIN { FS=": " }  ;  {print $2}' | head -1)
    case "$1" in
        auto|-a|reset|-r) 
               smc -k "FS! " -w 0000
               echo Fan speed is set to auto mode ;;
         set|-s) echo Total fans amount: $FANSTOTAL
               for i in $(seq 1 $FANSTOTAL); do
                   smc -k "FS! " -w 0003
                   smc -k F`expr $i - 1`Tg -w `printf '%x\n' $(expr $RPM \* 4)`
               done
               echo Fan speed is set to $RPM ;;
           *)  smc -f;;
esac
}

```

Описание:

* `fan set 3500` установит скорость 3500 RPM для каждого вентилятора в системе.

* `fan auto` вернет режим работы вентиляторов по умолчанию 

* `fan` с любыми другими параметрами или с пустым аргументом просто покажет информацию о текущем состоянии вентиляторов.


Кстати, вместо функции в bash profile, можно добавить скрипт в /usr/local/bin.

`vim /usr/local/bin/fanfun`


```
#!/bin/bash
set -e
FANSTOTAL=$(smc -f | awk  'BEGIN { FS=": " }  ;  {print $2}' | head -1)
RPM=$2
case "$1" in
    
     auto|-a|reset|-r)
           smc -k "FS! " -w 0000
           echo Fan speed is set to auto mode;;
     
     set|-s)
           echo Total fans amount: $FANSTOTAL
           for i in $(seq 1 $FANSTOTAL); do
               smc -k "FS! " -w 0003
               smc -k F`expr $i - 1`Tg -w `printf '%x\n' $(expr $RPM \* 4)`
           done
           echo Fan speed is set to $RPM ;;
     
     help|-h) 
           echo "----------------------"
           echo "'fan set <number>' or 'fan -s <number>' to force fan speed"
           echo "'fan reset' or 'fan -r' to reset fan status to default"
           echo "----------------------"
           smc -f;;
           
       *)  smc -f;;
esac

```

В этом случае надо будет сделать симлинк на программу smc.  

`ln -s /Applications/smcFanControl.app/Contents/Resources/smc /usr/local/bin/smc`

А также сделать скрипт исполняемым:

`chmod +x /usr/local/bin/fanfun`
