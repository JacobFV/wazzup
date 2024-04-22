import pytest
from core.sampling_and_generation import Sampler, DraftGenerator
from database.models import User, Message, SamplingConfig, GenerationConfig

def test_sample_messages():
    user = User(username="testuser", email="testuser@example.com", password_hash="password")
    config = SamplingConfig(recency_weight=0.5, diversity_weight=0.2, complexity_weight=0.2, alignment_weight=0.1)
    sampler = Sampler()
    messages = sampler.sample_messages(user.id, config)
    # Assert that messages are sampled correctly

def test_generate_draft():
    user = User(username="testuser", email="testuser@example.com", password_hash="password")
    messages = [Message(content="Test message 1"), Message(content="Test message 2")]
    config = GenerationConfig(max_tokens=100, temperature=0.7, top_p=0.9, frequency_penalty=0.1, presence_penalty=0.1)
    generator = DraftGenerator()
    draft = generator.generate_draft(user.id, messages, config)
    # Assert that draft is generated correctly

