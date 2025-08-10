# RAIA – Robô Social 🤖

RAIA é um **robô social e afetivo** desenvolvido para interagir de forma natural e acolhedora com qualquer pessoa, com atenção especial a proporcionar comunicação segura, clara e confortável para pessoas autistas.  

Diferente de assistentes virtuais comuns, a RAIA apresenta **comportamento proativo**: ela pode iniciar conversas, demonstrar interesse genuíno, adaptar seu tom de voz e ritmo para criar interações mais confortáveis e acessíveis.

---

## 📌 Principais Funcionalidades
- **Interação natural:** conversas fluidas e personalizadas.
- **Comportamento proativo:** inicia diálogos com perguntas pré-definidas como *"Como você está?"* e *"Quem é você?"*.
- **Foco em acessibilidade:** comunicação adaptada para pessoas autistas, evitando excesso de estímulos e linguagem ambígua.
- **Ativação por Wakeface:** RAIA reconhece quando o usuário está presente ao olhar para ele.
- **Compatibilidade multilíngue:** fácil adaptação para outros idiomas.

---

## 🛠 Estrutura de Hardware

A RAIA é baseada na plataforma robótica EVA, mas com modificações para otimizar sua função social e afetiva.  

**Componentes utilizados:**
- 🖥️ [Tela Waveshare 7inch HDMI LCD (H)](https://www.waveshare.com/7inch-HDMI-LCD-H.htm) – Exibição de expressões e informações.
- 📷 [Câmera IMX219-160IR](https://www.waveshare.com/wiki/IMX219-160IR_Camera) – Reconhecimento visual.
- 🎙️ [ReSpeaker Mic Array v2.0](https://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/) – Captação de áudio.
- 🔊 [Caixas de som](https://www.waveshare.com/8ohm-5w-speaker.htm) – Saída de áudio.
- 🤖 [Raspberry Pi 5 4GB](https://www.waveshare.com/raspberry-pi-5.htm?sku=30141) – Unidade de processamento.
- 🔃 [2x Motores de passo 28BYJ-48](https://www.prometec.net/motor-28byj-48/) – Movimento do pescoço.
- 💡 [Anel LED RGB Neopixel 24 bits WS2812](https://www.amazon.es/dp/B07QLMPV6S) – Feedback visual.
- 📡 [ESP-WROOM-32](https://www.amazon.es/dp/B071P98VTG) + [Projeto WLED](https://github.com/wled-dev/WLED) – Controle dos LEDs.
- 🪭 [Ventoinha Noctua NF-A8 5V PWM](https://www.amazon.es/dp/B07DXMF32M) – Refrigeração.
- 🖨️ Estrutura plástica impressa em 3D (**WIP – Modelos serão disponibilizados**).

---

## ⚙️ Instalação

### 1️⃣ Pré-requisitos
Certifique-se de ter o **Python 3.9+** instalado e o `pip` configurado.  

Clone o repositório e instale as dependências:
```bash
git clone https://github.com/seuusuario/RAIA-Social-Robot.git
cd RAIA-Social-Robot
pip3 install -r requirements.txt
```

### 2️⃣ Configuração de Serviços Google e OpenAI
A RAIA utiliza APIs de:

Google Speech-to-Text<br>
Google Text-to-Speech<br>
OpenAI GPT para geração de diálogo<br>

#### Passos:
Crie contas no Google Cloud e OpenAI.
Gere as chaves de API necessárias.
Salve o arquivo de credenciais do Google em:

```bash
$ qualquer_diretorio
.
├── credentials
│   └── google_credentials.json
└── RAIA-Social-Robot/
```

##### Configure as variáveis de ambiente:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/caminho/para/credentials/google_credentials.json"
export OPENAI_API_KEY="sua_chave_openai"
```
<b>Nota</b>: O arquivo Shara_prompt.txt contém as instruções da RAIA totalmente em português.
Para usar outro idioma, edite o prompt e as configurações de idioma do Google Cloud.
## 🚀 Uso
### Para iniciar a RAIA:
```bash
python3 main.py
```

<h3>👥 Equipe de Desenvolvimento</h3>

<p><strong>Alunos:</strong></p>
<ul>
  <li>Aníbal Siqueira Manso Monteiro (Info D)</li>
  <li>Augusto Gonçalves Lemos (Info F)</li>
  <li>Davi Vinagre Dias (Info F)</li>
  <li>Gustavo Porto (Info F)</li>
  <li>Higor Machado Miranda (Info F)</li>
  <li>Iago Diniz Sepini Nunes (Info E)</li>
  <li>Igor Garcia (Info G)</li>
  <li>Mateus Gonçalves Tavares (Info B)</li>
  <li>Thales Silva Garcia (Info B)</li>
  <li>Tiago Masaro Carvalho (Info G)</li>
  <li>Vinicius Yuji Ozawa (Info E)</li>
  <li>Wellington Laneto Luciano (Info G)</li>
</ul>

<p><strong>Professor Orientador:</strong><br>Matheus Franco</p>

<p><em>Este repositório foi clonado a partir do projeto original 
<a href="https://github.com/Laura-VFA/Proactive-Shara-Robot" target="_blank">Proactive Shara Robot</a> 
para fins exclusivamente acadêmicos.</em></p>
