import { OnHomePageHandler } from '@metamask/snaps-sdk';
import { panel, text, divider, heading } from '@metamask/snaps-sdk';

export const onHomePage: OnHomePageHandler = async () => {
  return {
    content: panel([
      heading('Synthesis Alpha'),
      text('**Impact Trading Agent** running autonomously on Base Sepolia.'),
      divider(),
      text('**Agent Status:** 🟢 Active on Base'),
      text('**Total Social Impact:** 0.042 ETH'),
      text('**Latest Dividend:** Sent to +1408555****'),
      divider(),
      text('Securing the network, supporting the community. 🌱')
    ]),
  };
};
