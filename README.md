# 🚌 Automação de Alerta: Carris Metropolitana

Este é um script em Python desenhado para quem não quer perder o autocarro nem perder tempo à espera na paragem. Ele monitoriza os dados em tempo real da **Carris Metropolitana** (via GTFS-Realtime) e avisa o momento exato em que deves sair de casa.

---

## 📋 Funcionalidades

- **Agendamento Inteligente**: O script fica em "espera" até à hora programada para o teu turno ou saída habitual.
- **Dados em Tempo Real**: Utiliza a API V2 da Carris Metropolitana para obter a localização exata dos veículos.
- **Filtro de Precisão**: Só dispara o alerta se o autocarro estiver em movimento (`speed > 0`) e destinado à tua paragem específica.
- **Encerramento Automático**: O script para de correr após uma janela de tempo definida para poupar recursos.

---

## 🛠️ Instalação e Requisitos

Antes de correr o script, precisas de instalar as bibliotecas necessárias:

```bash
pip install requests google-transit-format

```
## 📡 Sobre a API

Este script utiliza a V2 da API da Carris Metropolitana, especificamente o endpoint de veículos:
https://api.carrismetropolitana.pt/v2/vehicles.pb

## ⚖️ Licença

Este projeto é para uso pessoal e educativo. Sê gentil com a API e evita colocar intervalos de time.sleep inferiores a 30 segundos para não sobrecarregar os servidores.
