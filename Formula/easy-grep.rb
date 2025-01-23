class EasyGrep < Formula
  include Language::Python::Virtualenv

  desc "Natural language to command line converter tool"
  homepage "https://github.com/mohammadkazem-sadoughi/easy-grep"
  url "https://github.com/mohammadkazem-sadoughi/easy-grep/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "PLACEHOLDER_SHA256" # You'll update this after creating the release
  license "MIT"

  depends_on "python@3.11"

  resource "click" do
    url "https://files.pythonhosted.org/packages/96/d3/f04c7bfcf5c1862a2a5b845c6b2b360488cf47af55dfa79c98f6a6bf98b5/click-8.1.7.tar.gz"
    sha256 "ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de"
  end

  resource "anthropic" do
    url "https://files.pythonhosted.org/packages/d9/d5/a1bd0d5f2a0a59ab16d25b28b3bea7e2e108e3b92a9b2f7c0e8f6c1a5a3/anthropic-0.21.3.tar.gz"
    sha256 "f1d9c3e90f8f8d5e0c2c4c70f70d7c2a7a3d5a2c8c4c7c5e8d8a9c7c1c1c1c1c"
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    system bin/"e-g", "--help"
  end
end 