from flask import Flask, request, Response, render_template
from openai import OpenAI
import logging
import os

# 获取项目根目录路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, 
           template_folder=os.path.join(project_root, 'templates'),
           static_folder=os.path.join(project_root, 'static'))
logging.basicConfig(level=logging.DEBUG)

# OpenRouter API Configuration (免费DeepSeek-R1模型)
OPENROUTER_API_KEY = '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'
OPENROUTER_BASE_URL = 'https://openrouter.ai/api/v1'

# Initialize OpenAI client for OpenRouter
client = OpenAI(
    base_url=OPENROUTER_BASE_URL,
    api_key=OPENROUTER_API_KEY
)

@app.route('/bingte')
def index():
    return render_template('index.html')

@app.route('/gen', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    app.logger.debug(f"Received prompt for gen: {prompt}")
    
    def generate_stream():
        try:
            completion = client.chat.completions.create(
                model="deepseek/deepseek-r1",
                messages=[{"role": "user", "content": prompt}],
                stream=True,
                temperature=0.7
            )
            
            app.logger.debug("Stream created successfully for gen")
            
            for chunk in completion:
                if chunk.choices[0].delta.content is not None:
                    app.logger.debug(f"Yielding chunk: {chunk.choices[0].delta.content}")
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            error_msg = f"Error in generate_stream: {str(e)}"
            app.logger.error(error_msg)
            yield error_msg
    
    return Response(generate_stream(), mimetype='text/plain')

@app.route('/gen2', methods=['POST'])
def generate2():
    data = request.json
    prompt = data.get('prompt', '')
    app.logger.debug(f"Received prompt for gen2: {prompt}")
    
    def generate_stream():
        try:
            completion = client.chat.completions.create(
                model="deepseek/deepseek-r1",
                messages=[{"role": "user", "content": prompt}],
                stream=True,
                temperature=0.8  # 稍微高一点的创造性
            )
            
            app.logger.debug("Stream created successfully for gen2")
            
            for chunk in completion:
                if chunk.choices[0].delta.content is not None:
                    app.logger.debug(f"Yielding chunk: {chunk.choices[0].delta.content}")
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            error_msg = f"Error in generate_stream: {str(e)}"
            app.logger.error(error_msg)
            yield error_msg
    
    return Response(generate_stream(), mimetype='text/plain')

@app.route('/gen3', methods=['POST'])
def generate3():
    data = request.json
    prompt = data.get('prompt', '')
    app.logger.debug(f"Received prompt for gen3: {prompt}")
    
    def generate_stream():
        try:
            completion = client.chat.completions.create(
                model="deepseek/deepseek-r1",
                messages=[{"role": "user", "content": prompt}],
                stream=True,
                temperature=0.9  # 更高的创造性用于创意生成
            )
            
            app.logger.debug("Stream created successfully for gen3")
            
            for chunk in completion:
                if chunk.choices[0].delta.content is not None:
                    app.logger.debug(f"Yielding chunk: {chunk.choices[0].delta.content}")
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            error_msg = f"Error in generate_stream: {str(e)}"
            app.logger.error(error_msg)
            yield error_msg
    
    return Response(generate_stream(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, port=60001, host="0.0.0.0")
