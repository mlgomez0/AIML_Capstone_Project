import { render, screen } from '@testing-library/react';
import App from './App';

test('renders hello world message', () => {
  render(<App />);
  const hello = screen.getByText(/Hello World/i);
  expect(hello).toBeInTheDocument();
});
